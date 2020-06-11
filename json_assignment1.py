from urllib.request import urlopen
import json
import ssl
sum=0
count=0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
total=0
url=input('Enter URL- ')
data=urlopen(url,context=ctx).read()
info = json.loads(data)["comments"]
#print(info)
for num in info:
    sum=sum+int(num["count"])
    count=count+1
print("Sum ",sum)
print("Count ",count)
