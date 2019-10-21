# headless
Strip headers from full-text documents in HathiTrust 

## Installation

```
pip install git+https://github.com/senderle/headless#egg=headless
```

## Usage

The API consists of one function at the moment, `load_pages`. 

It accepts a path to a zip file or directory of text files, which
it assumes are single-page documents from a HathiTrust volume. 

It returns a list of strings, each of which is a page from the volume
with headers stripped using a lightly modified version of Ted Underwood's
[HeaderFinder](https://github.com/tedunderwood/DataMunging/tree/master/runningheaders) code
(released with permission from [@tedunderwood](https://github.com/tedunderwood)).

```
from headless import load_pages
pages = load_pages('path/to/htarchive_dir_or.zip')
```
