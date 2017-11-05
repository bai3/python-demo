# -*- coding: UTF-8 -*-
import urllib2


user_agent = "'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT6.1; Trident/5.0;"
header = {'User-Agent': user_agent}
res = urllib2.Request('http://39.108.84.239')
response = urllib2.urlopen(res)
print response.read()
