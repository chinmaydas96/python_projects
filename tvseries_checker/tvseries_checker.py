import mechanize
URL = 'http://tvseries.in'
tv_show="Arrow S04E15" 
def my_tv_series():
	b=mechanize.browser()
	fd=b.open(URL)
	return x in fd.read()

if __name__ == '__main__':
		if my_tv_series():
			print 'yes'
		else:
			print "no"
