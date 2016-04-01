import requests
from bs4 import BeautifulSoup
urls = "https://www.udemy.com/courses/search/?q=python&src=sug&lang=en&p="
url = [urls + str(num) for num in range(1,13)]
ans = []

def scrape(url):
	r=requests.get(url)
	soup=BeautifulSoup(r.content)
	for i in soup.findAll("span",{"class":"title bold fs15-force ng-binding"}):
		u=i.text
		ans.append(u)
count = 1 		
for i in url:
	scrape(i)
	print "DONE :" + str(count)
	count +=1
f =  open("g.txt",'w')
for j in ans:
	f.write("."+j+"\n")

