import mechanize
from bs4 import BeautifulSoup
br=mechanize.Browser()
br.addheaders = [('User-agent', 'Firefox')]
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
url="http://time.is"
respose=br.open(url)
a=respose.read()
soup=BeautifulSoup(a)
s=soup.find_all("div",{'id':'twd'})
print s[0].text
