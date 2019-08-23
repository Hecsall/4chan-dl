#!/usr/bin/python3

import argparse
import os
from io import open as iopen
import urllib3
urllib3.disable_warnings()
from urllib.parse import urlsplit
from html.parser import HTMLParser


#Create directory function
def create_dir(folder):
	i = 1
	tmp, remaining_folder_list = folder.split("/",i) #first split
	tmp2 = ''.join(tmp)
	check = 0  #exit while counter
	path = "/" + tmp2
	while(check != 1):
		os.chdir(path)
		path + "/"
		i + 1
		if("/" in remaining_folder_list): #checking if it is last dir
			tmp, remaining_folder_list = remaining_folder_list.split("/", 1)
			#print (tmp)
			tmp2 = ''.join(tmp)
			path = path + "/" + tmp2	
		else:    #last dir
			tmp2 = ''.join(remaining_folder_list)
			path = path + "/" + tmp2
			if not os.path.exists(path):  #if doesn't exists create dir
				os.mkdir(path)
			check = 1 #exit while
	return path



# HTML Parser -> Finding images in the thread
class ThreadParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.images = []
		self.counter = 0

	def handle_starttag(self, tag, attrs):
		images = []
		if tag=="a" and "class" in dict(attrs) and dict(attrs)["class"] == "fileThumb":
			self.images.append("https:" + str(dict(attrs)["href"]))
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
	flag = 0

	# Check if the page responds correctly (not 404 or other errors)
	if r.status == 200:
		parser = ThreadParser()
		html = str(r.data)
		parser.feed(html)

		# Manage the directory name
		if directoryName == "threadDirectory":
			tmpName = urlsplit(threadUrl)[2].split('/')
			directory = str(tmpName[-1 if tmpName[-1] != '' else -2])
			flag = 1
		else:
			directory = directoryName[1:] if directoryName[0] == '/' else directoryName

		# Check if images are found
		if parser.counter == 0:
			print("No images found!")
			return
		else:
			print("Found {} images! Download starting in directory \"{}\"\n".format(parser.counter, directory))

		# Creates the directory
		if (flag == 1):
			os.makedirs(directory)
		else:
			directory = create_dir(directory)	

		# Check if limit is set
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
	parser.add_argument ('-o', '--output', default='threadDirectory', help='Directory name where the script saves the images. Default directory name will be the thread id.')
	parser.add_argument ('-l', '--limit', default=0, type=int, help='Limit how many images to download.')

	args = parser.parse_args()

	main(*args.url, args.output, args.limit)
    