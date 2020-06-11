from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
total=0
url=input('Enter URL')
data=urlopen(url,context=ctx).read()
tree = ET.fromstring(data)
results = tree.findall('comments/comment')
for result in results:
    num=int(result.find('count').text)
    total=total+num
print(total)
