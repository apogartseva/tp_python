#!/usr/bin/env python

import cgi
import cgitb


# explicit CGI errors 
cgitb.enable()  


print("Content-type: text/html\n")

# parse the query parameters
form = cgi.FieldStorage()
name = form.getvalue("name", "")

# HTML content
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>TP 7</title>
</head>
<body>
    <h1>Bonjour, {name}!</h1>
</body>
</html>
"""
print(html_content)
