# 4chan-dl
Simple 4chan image downloader

Could be better written, but for now it works.


### Usage
python3 4chan-dl.py [-h] [-o OUTPUT] [-l LIMIT] url [url ...]

Downloads 4chan thread images.

positional arguments:
	url                   4chan thread URL

optional arguments:
	-h, --help											show this help message and exit
	-o OUTPUT, --output OUTPUT			Directory name where the script saves the images.
																	Default directory name will be the thread id
	-l LIMIT, --limit LIMIT					Limit how many images to download
