from StringIO import StringIO    
import pycurl
from bs4 import BeautifulSoup
import os,csv
print "location is usally written like '/Users/James/Desktop'"
Location=input("input location to save csv (use quotes)")
page=15
Bigdata=[]
nameRows=[]
row=[]
str2="_"
#redo
url='http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591&postdays=0&postorder=asc&start='
def insertData(data,namesAndNumbers,index):
       data[index][0]= namesAndNumbers[index].a["name"]
       data[index][1]=namesAndNumbers[index].get_text()
       return data
def goThroughPages(url,d,:
       pages=page*d
       url=url+str(pages)
       for d in range(0,9):
       storage = StringIO()
       c = pycurl.Curl()
       c.setopt(c.URL, url)
       c.setopt(c.WRITEFUNCTION, storage.write)
       c.setopt(c.FOLLOWLOCATION, True)
       c.perform()
       c.close()
       content = storage.getvalue()
       soup=BeautifulSoup(content, 'html.parser')
       bText=soup.find_all("span",class_="postbody")
       namesAndNumbers=soup.find_all("span",class_="name")
       nameRows.append(len(namesAndNumbers))
       dates= soup.find_all("span",class_="postdetails")
       data=[[0 for i in range(4)] for j in range(len(namesAndNumbers))] 
       for i in range(0,len(namesAndNumbers)):
              insertData(data)   
       j=0
       for i in range(0,len(namesAndNumbers)):
              if len(row)==83:
                     j=j+1
              if len(row)==76 or len(row)==78 :
                     j=j+2
              if len(row)==79:
                     j=j+3
              if bText[j].get_text()!='' and bText[j].get_text() not  in row:
                     data[i][2] =bText[j].get_text()
              elif bText[j].get_text()!='':
                     while bText[j].get_text()  in row:
                            j=j+1
                     data[i][2] =bText[j].get_text()
              else:
                     j=j+1
                     while bText[j].get_text() in row:
                            j=j+1       
                     data[i][2]=bText[j].get_text()
              if str2 in data[i][2]:
                      Place= bText[j].get_text().index(str2)              
                      data[i][2]=(bText[j].get_text()[0:Place])  
              row.append(data[i][2])
              j=j+1
       for i in range(0,len(dates)/2):
             data[i][3]=dates[1+2*i].get_text()[0:34]
       Bigdata.append(data)
       writeToFile(nameRows,Bigdata)
def writeToFile(nameRows,Bigdata):
       os.chdir(Location)
       with open("forum.csv", "w") as toWrite:
          writer = csv.writer(toWrite, delimiter=",")
          writer.writerow(["number","name", "date", "post"])
          for a in range(0,9):
              for b in range(0,nameRows[a]):
               writer.writerow([Bigdata[a][b][0],Bigdata[a][b][1],Bigdata[a][b][3].encode("utf-8"),Bigdata[a][b][2].encode("utf-8")])



       
