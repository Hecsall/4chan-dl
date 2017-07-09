#!/usr/bin/python

import requests
from lxml import html
from io import open as iopen
from urllib.parse import urlsplit


def requests_image(file_url):
	file_name =  urlsplit(file_url)[2].split('/')[-1]
	image = requests.get(file_url)
	if image.status_code == requests.codes.ok:
		with iopen(file_name, 'wb') as file:
			file.write(image.content)
			print("> Image {} downloaded ({}/{})".format(file_name, index, len(images_links)))


print(""" \n
  ██╗  ██╗ ██████╗██╗  ██╗ █████╗ ███╗   ██╗
  ██║  ██║██╔════╝██║  ██║██╔══██╗████╗  ██║
  ███████║██║     ███████║███████║██╔██╗ ██║
  ╚════██║██║     ██╔══██║██╔══██║██║╚██╗██║
       ██║╚██████╗██║  ██║██║  ██║██║ ╚████║
       ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
""")


thread_url = input("Insert Thread URL: ")

thread = requests.get(thread_url)
html = html.fromstring(thread.content)
images_links = html.xpath("//div[@class='board']//a[@class='fileThumb']/@href")

print("\n{} images found".format(len(images_links)))
print("Download starting, please wait...")

index = 0
for link in images_links:
	index += 1
	requests_image("http:" + str(link))

print("\nSuccessfully downloaded {} images! (Probably)".format(len(images_links)))
