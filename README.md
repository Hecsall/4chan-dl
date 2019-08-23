# 4chan-dl
Simple 4chan image downloader.

Could be better written, but for now it works.

**NOTICE: this only works with Python 3**

## Usage
python3 4chan-dl.py [-h] [-o OUTPUT] [-l LIMIT] url [url ...]

Tested with urls like:
* http://boards.4chan.org/a/
* http://boards.4chan.org/a/thread/123456789
* https://yuki.la/jp/page/23541

#### Positional arguments:

* **url**  4chan thread URL


#### Optional arguments:

* **-h, --help**  show this help message and exit
* **-o OUTPUT, --output OUTPUT**  Path where the script saves the images. Default will create a directory in the project folder and directory name will be the thread id
* **-l LIMIT, --limit LIMIT**  Limit how many images to download.