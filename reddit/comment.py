import mechanize
from bs4 import BeautifulSoup
br = mechanize.Browser()
br.addheaders = [('User-agent', 'Firefox')]
br.set_handle_robots(False)   # ignore robots
URL = "https://www.reddit.com/r/pics/comments/4epf6l/this_guy_got_himself_an_interesting_planetary/"
respose = br.open(URL)
a = respose.read()
soup = BeautifulSoup(a)
s = soup.findAll("div", {"class": "md"})
count = 1
for i in s:
	b = i.findAll("p")
	for j in b:
		print str(count) + "." + j.text + "\n"
		count +=1