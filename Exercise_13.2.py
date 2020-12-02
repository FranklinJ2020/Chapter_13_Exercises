import urllib.request as link
import json

url = input("Enter url: ")
data = link.urlopen(url).read().decode('utf-8')
object = json.loads(data)

sum = 0
count = 0

for comment in object["comments"]:
    sum += int(comment["count"])
    count += 1

print('Count: ', count)
print('Sum: ', sum)
