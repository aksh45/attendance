import getpass
from tabulate import tabulate
import requests
from bs4 import BeautifulSoup
usn=input("Enter username")
passw=getpass.getpass("Enter password")
payload={"username":usn,"password":passw}
r=requests.post("https://academics.gndec.ac.in/",data=payload)
values2={"Provisional Result":"in","final_exam_result_with_grades": "in"}
cookies=r.cookies
rpost2 = requests.post("https://academics.gndec.ac.in",cookies=cookies, data=values2)
soup=BeautifulSoup(rpost2.content,'html.parser')
subj=list(soup.find_all("td"))
subj1=[i.get_text() for i in subj]
elem=subj1.index('Grade')
fltp=subj1[5:122]
ls=len(fltp)//13
fl=[]
cn=0
for i in range(ls):
    lis=[]
    for z in range(13):
        lis.append(fltp[z+cn])
    cn+=13
    fl.append(lis)
print(tabulate(fl))

