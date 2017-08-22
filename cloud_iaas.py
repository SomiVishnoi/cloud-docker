#!/usr/bin/python2
import os,cgi,commands

print "content-type: text/html"
#print

choice=cgi.FormContent()['choice'][0]
if choice=='qcow':
	print "location: ../cloud_qcow.html"
	print
elif choice=='block':
	print "location: ../cloud_iaas_start2.html"
	print
