

#!/usr/bin/python
import cgi

print "Content-type:text/html"
print '<html>'
print '<head><title>CGI Program</title></head>'
print '<body>'

form = cgi.FieldStorage()
if form.getvalue("name"):
	name = form.getvalue("name")
	print '<h1>Hello ' + name + '! Thanks for using my script!</h1><br />'
if form.getvalue("happy"):
	print "<p> Yay! I'm happy too! </p>"
if form.getvalue("sad"):
	print "<p> Oh no! Why are you sad? </p>"

print '<form method="post" action="hello.py">'
print '<p>Name: <input type="text" name="name"/></p>'
print '<input type="checkbox" name="happy" /> Happy'
print '<input type="checkbox" name="sad" /> Sad'
print '<input type="submit" value="Submit" />'
print '</form>'
print '</body>'
print '</html>'
