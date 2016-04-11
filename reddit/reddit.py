import mechanize
import re
import datetime
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.addheaders = [('User-agent', 'Firefox')]
br.set_handle_robots(False)   # ignore robots
URL=" https://www.reddit.com"
respose=br.open(URL)
a=respose.read()
soup=BeautifulSoup(a)
s=soup.findAll("div",{"onclick":"click_thing(this)","data-type":"link"})

class reddit(object):
    def __init__(self,title,url,author,no_comments,time,upvote):
		self.title=title
		self.url=url
		self.author=author
		self.no_comments=no_comments
		self.time=time
		self.upvote = upvote

    def __repr__(self):
        return str(self.upvote)


x=[]
for i in s:
	title = i.find("a",{"class":"title may-blank "}).text
	url =  i.find("a",{"class":"title may-blank "})["href"]
	if url.startswith("/r/"):
		url = URL + url
	author = i.find("p",{"class":"tagline"}).find("a").text
	no_comments = i.find("a",{"data-event-action":"comments"}).text
	try:	
		no_comments = int( no_comments.split(" ")[0])
	except:
		no_comments = 0
	# time = i.find("time")["datetime"]
	time = str(i['data-timestamp'])[:-3]
	time = datetime.datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S')
	upvote = i.find("div",{"class":"score unvoted"}).text
	r = reddit(title,url,author,no_comments,time,upvote)
	x.append(r)	
	print upvote
# from pprint import pprint
# print pprint(x)
