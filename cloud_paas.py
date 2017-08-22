#!/usr/bin/python2
import os
import commands
import cgi
print "Content-Type: text/html"
print

ch=cgi.FormContent()['ch'][0]
if ch=='py':
	print "<form action='/scripts/cloud_paas_python.py'>"
	print "<h2>Online Python Shell</h2>"
	print "Enter your commands:"
	print "<textarea cols='70' rows='20' name='txtm'></textarea>"
	print "<br />"
	print "<input type='submit' />"
	print "</form>"
elif ch=='java':
	print "<form action='/scripts/cloud_paas_java.py'>"
	print "<h2>Online Java Shell</h2>"
	print "Enter your commands:"
	print "<textarea cols='70' rows='20' name='txtm'></textarea>"
	print "<br />"
	print "<input type='submit' />"
	print "</form>"
elif ch=='php':
	print "<form action='/scripts/cloud_paas_php.py'>"
	print "<h2>Online PHP Shell</h2>"
	print "Enter your commands:"
	print "<textarea cols='70' rows='20' name='txtm'></textarea>"
	print "<br />"
	print "<input type='submit' />"
	print "</form>"


