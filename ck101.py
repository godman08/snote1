# -*- coding: utf-8 -*-
#基本 Frame -- 開始 --

import re
import os
import urllib2
import cookielib
import urllib
import codecs
'''
使用方法 : 
	from ck101 import CK101
	f=CK101()
	f.start(':BOOK_ID')
	
'''
class CK101():
	def __init__(self):
		print 'init...MYCODE'
		self.AGENT_1 = "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"
		self.url1="http://ck101.com/forum.php?mod=viewthread&tid=2791661&page=1"
		self.ck101A="http://ck101.com/forum.php?mod=threadlazydata&tid=2791661"
		self.ck101B="http://ck101.com/thread-2791661-2-1.html"
		self.html=''

	def start(self,BOOK_ID="2791661"):
		bookUrl = self.genBookUrl_1(BOOK_ID)
		html = self.urlRead(bookUrl)
		
		TITLE = self.getInfo(BOOK_ID,html)
		self.saveData(BOOK_ID,TITLE,html)
		self.html=html
		return TITLE


	# 傳入 BOOK_ID，產生網址，僅第一頁
	def genBookUrl_1(self,BOOK_ID="2791661",PAGE_ID=1):
		bookUrl = 'http://ck101.com/forum.php?mod=threadlazydata&tid=%s' % BOOK_ID
		return bookUrl
		
	# 傳入 BOOK_ID，產生網址，第二頁開始
	def genBookUrl(self,BOOK_ID="2791661",PAGE_ID=2):
		bookUrl = 'http://ck101.com/thread-%s-%s-1.html' % (BOOK_ID,PAGE_ID)
		return bookUrl

	def saveData(self,BOOK_ID,filename,data):
		filename = filename.decode('utf-8')
		filename = filename.split('-')[0]
		filename = filename.replace(u'作者：','_').replace(' ','')
		w=open('%s_%s.txt' % (BOOK_ID,filename),'w')
		w.write(data)
		w.close()
		print 'WRITE %s DONE...%s' % (filename,len(data))
		
	# if the folder not exist, create it
	def make_folder(self,folder_name):
		if not os.path.exists(folder_name):
			os.makedirs(folder_name)
			print '建立資料夾...<%s>' % folder_name

	def urlRead(self,url):
		return urllib2.urlopen(url).read()
		
	def urlReadwithAgent(self,url):
		req = urllib2.Request(url)
		req.add_header("User-Agent", "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11")
		res = urllib2.urlopen(req)
		return res.read()
	 	
	def getInfo(self,BOOK_ID,html):
		
		TITLE = BOOK_ID
		
		_title = re.findall('<title>([^<]+)<',html)
		if len(_title) > 0 :
			TITLE = _title[0]
		return TITLE



