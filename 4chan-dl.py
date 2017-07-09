#!/usr/bin/python
import argparse
import os
from io import open as iopen
import urllib3
from urllib.parse import urlsplit
from html.parser import HTMLParser



# HTML Parser -> Finding images in the thread
class ThreadParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.images = []
		self.counter = 0

	def handle_starttag(self, tag, attrs):
		images = []
		if tag=="a" and "class" in dict(attrs) and dict(attrs)["class"] == "fileThumb":
			self.images.append("http:" + str(dict(attrs)["href"]))
			self.counter += 1



# Function that downloads images
def imageDownloader(images, directory, limit=0):
	http = urllib3.PoolManager()
	index = 0
	for img in images[0:]:
		if index == limit and index != 0:
			break
		else:
			file_name =  urlsplit(img)[2].split('/')[-1]
			image = http.request('GET', img, headers={'User-Agent': 'Mozilla/5.0'})
			index += 1
			with iopen(directory + "/" + file_name, 'wb') as file:
				file.write(image.data)
				print("> Image {} downloaded ({}/{})".format(file_name, index, len(images) if limit == 0 else limit))



def main(threadUrl, directoryName, limit):
	print("""
  ██╗  ██╗ ██████╗██╗  ██╗ █████╗ ███╗   ██╗
  ██║  ██║██╔════╝██║  ██║██╔══██╗████╗  ██║
  ███████║██║     ███████║███████║██╔██╗ ██║
  ╚════██║██║     ██╔══██║██╔══██║██║╚██╗██║
       ██║╚██████╗██║  ██║██║  ██║██║ ╚████║
       ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝  by Hecsall
	""")

	http = urllib3.PoolManager()
	r = http.request('GET', threadUrl, headers={'User-Agent': 'Mozilla/5.0'})

	# Check if the page responds correctly (not 404 or other errors)
	if r.status == 200:
		parser = ThreadParser()
		html = str(r.data)
		parser.feed(html)

		# Manage the directory name
		if directoryName == "threadDirectory":
			directory = str(urlsplit(threadUrl)[2].split('/')[-1])
		else:
			directory = directoryName

		# Creates the directory
		if not os.path.exists(directory):
			os.makedirs(directory)

		print("Found {} images! Download starting in directory \"{}\"\n".format(parser.counter, directory))
		if limit != 0:
			print("Download limit set to {}\n".format(limit))

		# Pass image links to the downloader
		imageDownloader(parser.images, directory, limit)
		print("\nAll {} images downloaded!".format(parser.counter if limit == 0 else limit))

	else:
		print("Error loading the URL, ensure to write it correctly.")



if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Downloads 4chan thread images.')

	parser.add_argument ('url', nargs='+', help='4chan thread URL')
	parser.add_argument ('-o', '--output', default='threadDirectory', help='Directory name where the script saves the images. Default directory name will be the thread id')
	parser.add_argument ('-l', '--limit', default=0, type=int, help='Limit how many images to download')

	args = parser.parse_args()

	main(*args.url, args.output, args.limit)
