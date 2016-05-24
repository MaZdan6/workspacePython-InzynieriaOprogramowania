from urllib import request

url = 'http://150.254.36.91/mt/cokupic.html'
opener = request . build_opener()
opener.addheaders = [('User - agent ','Mozilla /5.0 6( X11 ; U; Linux i686 ) Gecko /20071127 Firefox /2.0.0.11 ')]
request.install_opener(opener)
html_string = request.urlopen(url).read()

print(html_string)