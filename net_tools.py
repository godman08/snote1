#!/usr/bin/python2.7.2
# -*- coding: utf-8 -*-
import urllib2
import cStringIO
from lxml import etree

# url 取得 html 轉成 etree
def urlToEtree(url):
	return toEtree(getHtml(url))

#取得網頁內容
def getHtml(url):
	html=urllib2.urlopen(url).read();
	html=html.replace('&nbsp;',' ')
	return html

#html 轉成 etree
def toEtree(html):
	parser=etree.HTMLParser()
	tree=etree.parse(cStringIO.StringIO(html),parser)
	return tree