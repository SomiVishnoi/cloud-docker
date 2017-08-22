#!/usr/bin/python2
import os,cgi,commands

print "content-type: text/html"
#print

typ=cgi.FormContent()['storage'][0]
if typ == "object":
	print "location: ../cloud_obj.html"
	print
elif typ == "block":
	print "location: ../cloud_block.html"
	print
