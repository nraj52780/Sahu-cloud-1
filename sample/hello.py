'''
1. sudo apt-get install apache2
2. sudo vim /etc/apache2/sites-available/default // change the permission here.
3. sudo service apache2 restart
4. vim hello.py
5. sudo chmod 755 hello.py
'''


#!/usr/bin/python

print "Content-type:text/html"
print '<html>'
print '<head><title>CGI Program</title></head>'
print '<body>'
print '<p> It works!!! </p>'
for i in range(5):
	print '<h1>Hello World! ' + i + '</h2>'
print '</body>'
print '</html>'


