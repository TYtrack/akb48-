from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv

html = urlopen("https://www.akb48.co.jp/about/members/")


user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
headers={"User-Agent":user_agent,"PHPSESSID":"aukoo2il7657nduaiep60dmsn1"}
request=urllib2.Request(url,headers=headers)
response=urllib2.urlopen(request)
contents = response.read()


bsObj = BeautifulSoup(html)

nameList = bsObj.find("body").find("div",{"class":"memberList"}).findAll("h4",{"class":"memberListNamej"})
urlList_pre = bsObj.find("body").find("div",{"class":"memberList"}).findAll("a",{"href":re.compile("detail\.php\?mid")})
urlList=[]
for i in urlList_pre:
    i="https://www.akb48.co.jp/about/members/"+i.attrs["href"]
    print(i)
    urlList.append(str(i))

with open("AKB48.csv","a+") as csvfile:
    writer = csv.writer(csvfile)
    for j in range(0,len(urlList)):
        print(urlList[j])
        profileUrl=urlopen(urlList[j])
        bsProfile=BeautifulSoup(profileUrl)
        ul=bsProfile.find("div",{"class":"memberDetailProfileWrapper"}).findAll("p")
        print(ul[0].string)
        writer.writerow([nameList[j].text,ul[0].string,ul[1].string,ul[2].string,ul[3].string])
        
        
