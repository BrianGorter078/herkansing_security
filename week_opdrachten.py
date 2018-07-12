from flask import Flask, request, Response, make_response
import html
import json
app = Flask(__name__)

# Week 1 
# Write a small web application that shows the User-Agent header of HTTP requests (see for example:
# https://httpbin.org/headers). You should use a user-agent switcher (browser extension) to test your code.
# • What happens if you set a custom user-agent value of ‘<script>alert("Hi!")</script>’ (excluding open
# (‘) and close (’) quotes)? Fix any security issues that you find.

@app.route("/week1/")
def week1():
    return request.headers.get('User-Agent')


@app.route("/week1/fixed")
def week1_fixed():
    headers = list(map(lambda x: html.escape(x[1]), request.headers))
    return json.dumps(headers)

# Extend last week’s web application to persistently store all HTTP headers from HTTP requests that it
# gets. Next to the headers, show the count of the number of times that header has been received.
# • Get someone else’s source code and try to make their web application do something that it clearly should
# not be doing. Fix the problem and discuss your findings (not necessarily in that order) with the code’s
# author

@app.route("/week2/")
def week2():
    return request.headers.get('User-Agent')

@app.route("/week2/fixed")
def week2_fixed():
    response = make_response(html.escape(request.headers.get('User-Agent')))
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response
