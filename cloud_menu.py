#!/usr/bin/python
import cgi
import os,commands

print "content-type: text/html"
#print 

menuch=cgi.FormContent()['setup'][0]
if menuch == "staas":
	print "location: ../cloud_staas.html"
	print
elif menuch == "caas":
	print "location: ../docker_new.html"
	print
elif menuch == "iaas":
	print "location: ../cloud_iaas.html"
	print
elif menuch == "paas":
	print "location: ../cloud_paas.html"
	print
elif menuch == "saas":
	print "location: ../cloud_saas.html"
	print
