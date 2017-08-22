#!/usr/bin/python2
import cgi
import commands

print "Content-Type: text/html"
print

docname=cgi.FormContent()['doc'][0]
commands.getstatusoutput("sudo docker inspect  somi-centos-1 | jq '.[].State.Status'")

print "<a href='docker-status-.py'>status ur container</a>"
