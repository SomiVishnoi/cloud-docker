#!/usr/bin/python2
import os,commands,cgi

print "content-type: text/html"
print

btn=cgi.FormContent()['btn'][0]
#print btn

if btn=='http':
	print "<form action='docker_httpd.py'>"
	print "enter name for docker<input type='text' name='http' />"
	print "enter ip of client <input type='text' name='ip' />"
	print "<input type='submit' />"
	print "</form>"

elif btn=='nfs':
	print "<form action='docker_nfs.py'>"
	print "enter name for docker<input type='text' name='http' />"
	print "enter size for lvm<input type='text' name='size' />"
	print "enter ip of client <input type='text' name='ip' />"
	print "<input type='submit' />"
	print "</form>"


