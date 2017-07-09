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
* **-o OUTPUT, --output OUTPUT**  Directory name where the script saves the images. Default directory name will be the thread id
* **-l LIMIT, --limit LIMIT**  Limit how many images to download.


## Nice to know
Using the **-o** argument, will eventually remove leading "**/**" to prevent the script to write in your root directory for security purposes.
You will still be able to write paths like "**-o ../someFolder**".
