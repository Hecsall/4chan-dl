# 4chan-dl
Simple 4chan image downloader
Could be better written, but for now it works.

**NOTICE: this only works with Python 3**

### Usage
python3 4chan-dl.py [-h] [-o OUTPUT] [-l LIMIT] url [url ...]


#### Positional arguments:

* **url**  4chan thread URL

#### Optional arguments:

* **-h, --help**  show this help message and exit
* **-o OUTPUT, --output OUTPUT**  Directory name where the script saves the images. Default directory name will be the thread id
* **-l LIMIT, --limit LIMIT**  Limit how many images to download
