from urllib import request

url ='http://150.254.36.91/mt/cokupic.html'
html_string = request.urlopen(url).read()
print(html_string);