#! /bin/bash/python3

#opens example site
#9-2-16



import urllib.request
url = 'http://www.zf-world.com/en/index.html'
website = urllib.request.urlopen(url)
readurl = website.read().decode("utf-8")
print(readurl)
