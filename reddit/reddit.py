import mechanize
from bs4 import BeautifulSoup
br = mechanize.Browser()
br.addheaders = [('User-agent', 'Firefox')]
br.set_handle_robots(False)   # ignore robots
url=" https://www.reddit.com/ "
respose=br.open(url)
a=respose.read()
soup=BeautifulSoup(a)
a = soup.findAll("a",{"class":"title may-blank "})
b = [i.text for i in a]

class reddit(object):
    def __init__(self,name,url):
	    self.name=name
	    self.url=url
    
    def __repr__(self):
        return self.name	 + "\n"  

x=[]
for i in a:
	name = i.text
	url =  i["href"]
	r = reddit(name,url)
	x.append(r)

print x