#!/usr/bin/python2

import commands,os
import cgi

print "Content-Type: text/html"
#print 

sto=cgi.FormContent()['objst'][0]
if sto == "nfs":
	print "location: ../cloud_obj_nfs.html"
	print
elif sto == "sshfs":
	print "location: ../cloud_obj_sshfs.html"
	print
elif sto == "st_req":
	print "location: ../cloud_obj_req.html"
	print
#elif sto == "st_req":#
#	print "location ../cloud_obj_ex.html"
#elif sto == "st_req":
#	print "location ../cloud_obj_rm.html"
