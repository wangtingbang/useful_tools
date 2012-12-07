#coding=UTF-8
import re
import urllib2

home = 'http://sc2.178.com/list/pic.html'
patt_img_lst_pre = '<div class="list-section-contents"'
patt_img_lst_suf = '" title='
prefix= '<p style="text-align: center"><img name="_img" alt="" src="'
suffix= '" /></p>'

def get_img_url_list( home_url ):
	home_page = urllib2.urlopen( home_url )
	home_content = home_page.read()
	home_page.close()
	#print home_content
	patt = patt_img_lst_pre + '(.*?)href="(.*?)' + patt_img_lst_suf
	img_url_lst = re.compile( patt, re.DOTALL ).findall( home_content )
	ulst = []
	for url in img_url_lst:
		#print '0: ', url[0], '1:' + url[1]
		nice = url[1].split( '"' )
		ulst.append( nice[0] )
	#open( 'page.html', 'w' ).write( home_content )
	return ulst

def down_img( url, path ):

	if path is None:
		path = './imgs'
	ulst = nice_img_url( url )	
	import os
	os.system( 'cd ' + path )
	print 'down img using wget'
	os.system( 'wget ' + str(ulst) )
	'''
	for u in url:
		print u
		os.system( 'wget ' + u )
	'''

def nice_img_url( url ):
	#patt_img_pre = '<p style="text-align: center">'
	patt_img_pre = '<img name="_img"'
	patt_img_suf = '</p>'
	patt = patt_img_pre + '(.*?)src=(.*?)' + patt_img_suf
	page = urllib2.urlopen( url )
	content = page.read()
	page.close()
	rough_url = re.compile( patt, re.DOTALL ).findall( content )
	s = rough_url[0]
	print 'rough img url: ', s
	patt_nice = 'http(.*?)jpg'
	url_str = re.compile( patt_nice, re.DOTALL ).findall( s[0] )
	img_url = url_str #.split( '"' )[0]
	print 'img url: ', img_url
	ulst = img_url + '.jpg'
	'''
	for u in img_url:
		nice = u[1].split('"')[0]
		ulst.append( nice )
	'''
	return ulst	


if __name__ == '__main__':
	ulst = get_img_url_list( home )

	if ulst is None:
		print 'url list is null'
		exit()
	down_img( ulst[0], '' )
	#for u in ulst:
		#down_img( u, '' )
		#print u
