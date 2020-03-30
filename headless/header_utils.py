# headless.py
#
# This is a lightly modified version of the HeaderFinder.py script form
# Ted Underwood's Data Munging repo:
#     https://github.com/tedunderwood/DataMunging
#
# That repo doesn't have a license, but I've received permission from Ted to
# use this and release it publicly.

import os
import glob
import zipfile

from codecs import decode

from htrc.models import HtrcPage
from htrc.runningheaders import parse_page_structure

# These three functions are taken from HathiTrust example code; similarly
# unlicensed (to the best of my knowledge).


def _textfile_to_lines(file):
    with open(file, mode='r', encoding='UTF-8') as f:
        return [l.rstrip() for l in f.readlines()]


def volume_from_folder(folder):
    if not os.path.isdir(folder):
        raise ValueError("{} does not exist".format(folder))

    text_files = sorted([text_file for text_file
                         in glob.glob(os.path.join(folder, "*.txt"))])
    volume = list(map(_textfile_to_lines, text_files))

    return [HtrcPage(p) for p in volume]


def volume_from_zip(file):
    with zipfile.ZipFile(file) as z:
        volume = list()
        files = [file for file in sorted(z.namelist())
                 if file.endswith(".txt")]
        for textfile in files:
            with z.open(textfile) as zf:
                # This is quite lazy and relies on the fact that the
                # default encoding arg for `decode` is `utf-8`.
                # Would be better to accept and pass an encoding arg.
                lines = map(decode, zf.readlines())
                volume.append([l.rstrip() for l in lines])

        return [HtrcPage(p) for p in volume]


def load_pages(path):
    if os.path.isdir(path):
        vol = volume_from_folder(path)
    else:
        vol = volume_from_zip(path)

    pages = parse_page_structure(vol)
    return ['\n'.join(line for line in page.body) for page in pages]
