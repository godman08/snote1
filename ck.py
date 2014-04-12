#!/usr/bin/python2.5.2
# -*- coding: utf-8 -*-
class ck:
	def __init__(self):
		self.url='http://ck101.com/thread-%s-%d-%d.html';
		self.title='';
		self.html='';
	def auto(self,book_id,page_start=1,page_end=1):
		last_page=self.getTotalPages(book_id);
		if last_page>0:
			for page_id in xrange(1,last_page+1):
				url = self.url % (book_id,page_id,1)
				tree_html=net_tools.urlToEtree(url)
				self.parseChapter(tree_html,page_id)
			print u'完成'

	#get total pages
	def getTotalPages(self,book_id):
		url = self.url % (book_id,1,1)
		last_page=1
		try:
			tree_html=net_tools.urlToEtree(url)
			title=tree_html.xpath('//title/text()')[0].split(' ')[0]
			print 'TITLE:',title
			self.folder=title
			os_tools._mkdir(title)
			last_pages=tree_html.xpath('//a[@class="last"]/text()')
			print len(last_pages)
			if len(last_pages)<1:
				nxt = tree_html.xpath('//a[@class="nxt"]')
				last_page = nxt[0].getprevious.text
				return int(last_page)
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
		tree_target=tree.xpath('//td[@class="t_f"]/text()')
		f=codecs.open(u'%s//第%03d頁.txt' % (self.folder,page_id),'w','utf-8')
		f.write('\n'.join(tree_target))
		f.close()
		print u'第%d頁抓取完成...' % page_id
