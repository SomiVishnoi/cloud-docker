#!/usr/bin/python2
import os,cgi,commands

print "Content-Type: text/html"
print
text=cgi.FormContent()['txtm'][0]
#print text

f1=open('/webcontent/scripts/text.php','w')
f1.write(text)
f1.close()

a=commands.getstatusoutput("sudo php /webcontent/scripts/text.php")
print a
print "<br />"
print "<a href='../cloud_paas.html'>click here to go to menu</a>"

