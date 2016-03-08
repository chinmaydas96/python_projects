import urllib2
from urllib2 import urlopen
import re
import cookielib
from cookielib import CookieJar
import time

cj=CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders=[('User-agent','Mozilla/5.0')]

def main():
 	try:
 		page="http://rss.nytimes.com/services/xml/rss/nyt/InternationalHome.xml"
 		sourcecode=opener.open(page).read()
 		#print sourcecode
		try:
		    titles=re.findall(r'<title>(.*?)</title>',sourcecode)
		    links=re.findall(r'<link>(.*?)</link>',sourcecode)
		    for i in  zip(links,titles):
		    	print i
		    	print
		  #   for title in titles:
				# print title

		  #   for link in links:
				# print link


		except Exception, e:
			print str(e)
 		
 	except Exception, e:
 		print str(e)
main()				
