#!/usr/bin/python2
import os,cgi,commands

print "Content-Type: text/html"
print
text=cgi.FormContent()['txtm'][0]
#print text
#commands.getoutput("sudo docker start shell_online")

#os.system("sudo chown apache /files/text.txt")
f1=open('/webcontent/scripts/text.py','w')
f1.write(text)
f1.close()

#a=commands.getstatusoutput("sudo python /webcontent/scripts/text.py")
print a[1]
print "<br />"
print "<a href='../cloud_paas.html'>click here to go to menu</a>"

