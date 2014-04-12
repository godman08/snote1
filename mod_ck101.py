#!/usr/bin/python2.5.2
# -*- coding: utf-8 -*-
import codecs,urllib,urllib2,re,time,random,os
from lxml import etree
import os_tools as os_tools
import net_tools as net_tools
class ck:
	def __init__(self):
		self.url1='http://ck101.com/forum.php?mod=threadlazydata&tid=%s';
		self.urln='http://ck101.com/thread-%s-%d-%d.html';
		self.title=''
		self.html=''
		self.nxt=''
		self.mode ='ALL_PAGE'
	def auto(self,book_id,page_start=1,page_end=1):
		last_page=self.getTotalPages(book_id)
		if self.mode == "NEXT_PAGE":
			### 第一頁
			url = self.url1 % book_id
			htm = net_tools.getHtml(url)
			#tree_html=net_tools.urlToEtree(url)
			#tree_target=tree_html.xpath('//td[@class="t_f"]/text()')
			page_id = 1
			w=open(u'%s//第%03d頁.txt' % (self.folder,page_id),'w')
			w.write(htm)
			w.close()
			#tree_html=net_tools.urlToEtree(url)
			#self.parseChapter(tree_html,1)
			
			### 第二頁以後
			MAX_PAGE = 0
			nxt=last_page
			while len(nxt)>10 and MAX_PAGE<100:
				url = "http://ck101.com/" + nxt
				print 'url: %s ' % url
				page_id = re.findall('thread-\d+-(\d+)-1',url)[0]
				print 'page_id: %s ' % page_id
				tree_html=net_tools.urlToEtree(url)
				self.parseChapter(tree_html,page_id)
				nxt = tree_html.xpath('//a[@class="nxt"]')
				if nxt:
					print 'nxt:%s' % nxt
					nxt = nxt[0].attrib['href']
					MAX_PAGE =MAX_PAGE+1
				else:
					MAX_PAGE = 99999
		elif last_page>0:
			### 第一頁
			url = self.url1 % book_id
			tree_html = net_tools.urlToEtree(url)
			self.parseChapter(tree_html,1)
			### 第二頁以後
			for page_id in xrange(2,last_page+1):
				url = self.url % (book_id,page_id,1)
				tree_html=net_tools.urlToEtree(url)
				self.parseChapter(tree_html,page_id)
			print u'完成'

	#get total pages
	def getTotalPages(self,book_id):
		url = self.urln % (book_id,1,1)
		last_page=1
		try:
			tree_html=net_tools.urlToEtree(url)
			title=tree_html.xpath('//a[@id="thread_subject"]/text()')[0]
			title=title.replace(':','')
			print 'TITLE:',title
			self.folder=title
			os_tools._mkdir(title)
			last_pages=tree_html.xpath('//a[@class="last"]/text()')
			print len(last_pages)
			if len(last_pages)<1:
				self.mode= 'NEXT_PAGE'
				nxt = tree_html.xpath('//a[@class="nxt"]')[0].attrib['href']
				#last_page = nxt[0].getprevious.text
				print 'NEXT_PAGE: %s' % nxt
				return nxt
			try:
				last_page=re.findall(r'\d+',last_pages[0])[0]
			except:
				last_page=last_pages[0].split(' ')[-1]
		except:
			print u'取得總頁數發生錯誤，預設為10'
			return 10
		print u'取得總頁數:',last_page
		return int(last_page)
		
	#parse chapter:
	def parseChapter(self,tree,page_id):
		page_id = int(page_id)
		tree_target=tree.xpath('//td[@class="t_f"]/text()')
		f=codecs.open(u'%s//第%03d頁.txt' % (self.folder,page_id),'w','utf-8')
		f.write('\n'.join(tree_target))
		f.close()
		print u'第%d頁抓取完成...' % page_id
