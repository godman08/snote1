#!/usr/bin/python2.5.2
# -*- coding: utf-8 -*-
import os

#新增資料夾
def _mkdir(newdir):
	if os.path.isdir(newdir):
		pass
	elif os.path.isfile(newdir):
		raise OSError("a file with the same name as the desired " \
			"dir, '%s', already exists." % newdir)
	else:
		head, tail = os.path.split(newdir)
		if head and not os.path.isdir(head):
			_mkdir(head)
			print "_mkdir %s" % repr(newdir)
		if tail:
			os.mkdir(newdir)
			print '_mkdir:',newdir