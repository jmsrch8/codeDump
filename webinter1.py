#! /bin/bash/python3

#opens example site
#9-2-16


#http_proxy = 'nrt-proxy.america.zf-world.com:8080'

import urllib.request
user = 'z231479'
password = 'Afterme000#'

pass_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
topurl = 'http://nrt-web/'
url = 'http://nrt-web/usermanagement/index.html'

pass_mgr.add_password(None, topurl, user, password)
handler = urllib.request.HTTPBasicAuthHandler(pass_mgr)
opener = urllib.request.build_opener(handler)
opener.open(url)
urllib.request.install_opener(opener)
urllib.request.ProxyHandler(proxies={'http':'10.240.9.10:8080'})
website = urllib.request.urlopen(url)
print(website.read())
