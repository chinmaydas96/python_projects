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

#    ....:     

# In [36]: names
# Out[36]: 

# In [38]: for i in names:
#    ....:     print i.name
#    ....:     

# In [39]: for i in names:
#     print i.name
#    ....:     

# In [40]: 

# In [40]: ls

# In [41]: class reddit(object):
#    ....:     def __init__(self,name,no):
#    ....:         self.name=name
#    ....:         self.no=no
#    ....:         

# In [42]: reddit("hello",1)
# Out[42]: <__main__.reddit at 0x7f373c0eacd0>

# In [43]: a=reddit("hello",1)

# In [44]: a.
# a.name  a.no    

# In [44]: a.n
# a.name  a.no    

# In [44]: a.n
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-44-5c8d0223dac0> in <module>()
# ----> 1 a.n

# AttributeError: 'reddit' object has no attribute 'n'

# In [45]: a.name
# Out[45]: 'hello'

# In [46]: a.no
# Out[46]: 1


# In [47]: a.__dict__
# Out[47]: {'name': 'hello', 'no': 1}

# In [48]: for i in a:
#     r = Redditname(i)
#     names.append(r)
#    ....:     
# ----> 1 for i in a:
#       2     r = Redditname(i)
#       3     names.append(r)
#       4 

# TypeError: 'reddit' object is not iterable

# In [49]: for i in a:
#     r = Redditname(i)
#     q = Re
# Redditname      ReferenceError  

# In [49]: for i in a:
#     r = reddit.name(i)
#     q = 


