import pandas as pd
from openpyxl import Workbook
import urllib2
from django.utils.encoding import smart_str, smart_unicode
from bs4 import BeautifulSoup

#fileName="GeeksforGeeks.xlsx"
#SheetName="Arrays"
#quote_page = "https://www.geeksforgeeks.org/array-data-structure/"

with open('./setting.properties') as fp: 
    quote_page=str(fp.readline())
    fileName=str(fp.readline())
    SheetName=str(fp.readline())
quote_page.replace("\n","")
fileName.replace("\n","")
SheetName.replace("\n","")

print quote_page
print fileName
print SheetName

print "https://www.geeksforgeeks.org/array-data-structure/"
print "Arrays"
print "GeeksforGeeks.xlsx"

page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
li_list=soup.find_all('li')

pattern='"https://www.geeksforgeeks.org/"[A-Za-z]+'

count=1
wb = Workbook()
ws = wb.create_sheet(SheetName)
ws.title = SheetName

for something in li_list:
    for anchor_tag in something.find_all('a',href=True):
        link=str(anchor_tag['href'])
        if "https://www.geeksforgeeks.org/" not in link:
            continue
        text=smart_str(anchor_tag.string)
        if text.count(' ')<=3:
            continue
        ws.cell(row=count,column=1).value=text;
        ws.cell(row=count,column=2).value=link;
        count=count+1

wb.save(fileName)


