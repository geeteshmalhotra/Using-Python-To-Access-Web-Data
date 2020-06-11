from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
total=0
count=0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter URL')
html=urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')
tags=soup('span')
for tag in tags:
    num=tag.contents[0]
    count=count+1
    total=total+int(num)
print("Count ",count)
print("Sum ",total )

#for tag in tags:
   # Look at the parts of a tag
  # print 'TAG:',tag
  # print 'URL:',tag.get('href', None)
  # print 'Contents:',tag.contents[0]
  # print 'Attrs:',tag.attrs
