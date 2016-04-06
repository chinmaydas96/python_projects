import mechanize
from bs4 import BeautifulSoup
br = mechanize.Browser()
br.addheaders = [('User-agent', 'Firefox')]
br.set_handle_robots(False)   # ignore robots
url="https://www.reddit.com/"
respose=br.open(url)
a=respose.read()
soup=BeautifulSoup(a)
a = soup.findAll("a",{"class":"title may-blank "})
b = [i.text for i in a]

class reddit(object):
    def __init__(self,name,no):
	    self.name=name
	    self.no=no
count=1
hello=[]
for i in b:
	r = reddit(i,count)
	hello.append(r)
	count+=1

print hello
for i in hello:
	print i.no,i.name