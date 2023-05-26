import xml.etree.ElementTree as ET

tree = ET.parse("bank.xml")
root = tree.getroot()

rang = 0
for person in root.findall("person"):
    balance = int(person.find("balance").text)
    if balance <= 30000000:
        rang += 1


count = 0
for person in root.findall("person"):
    balance = int(person.find("balance").text)
    if balance >= 50000000:
        count += 1

rand = 0
for person in root.findall("person"):
    balance = int(person.find("balance").text)
    if 30000000 <= balance <= 40000000:
        rand += 1


for person in root.findall("person"):
     if  int(person.find("balance").text) >= 50000000:
        print("name of customer:" ,person.find("name").text)
       # print("lastname of customer:", person.find("last-name").text)

print(rang)
print(count)
print(rand)
