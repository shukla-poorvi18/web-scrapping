from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
from lxml import html
import json

print("Application Started plz minimize chrome and only open it while seeing captcha")  
driver = webdriver.Chrome(r"C:\webdriver\chromedriver") 
 
  
 
driver.get("https://parivahan.gov.in/rcdlstatus/?pur_cd=101")

str = input("Enter Driving License No.: ")
driver.find_element_by_name("form_rcdl:tf_dlNO").send_keys(str)  
time.sleep(1)  

str = input("Enter DOB: ")
driver.find_element_by_name("form_rcdl:tf_dob_input").send_keys(str)  
time.sleep(1)  

str = input("Enter CaptchaID : ")
driver.find_element_by_name("form_rcdl:j_idt32:CaptchaID").send_keys(str)  
time.sleep(1)  


driver.find_element_by_name("form_rcdl:j_idt43").send_keys(Keys.ENTER)  
time.sleep(1)


url= 'https://parivahan.gov.in/rcdlstatus/?pur_cd=101'
r=requests.get(url)
soup = BeautifulSoup(r.text,features='lxml') 
table = soup.find("table",class_="table table-responsive table-striped table-condensed table-bordered")
row = table.find_all('tr')
row_list = []
for tr in row:
    td = tr.find_all('td')
    for i in td:
        row = [i.text for i in td]
        row_list.append(row) 
    

with open("scrap1.json", "wb") as outfile: 
    json.dump(row_list, outfile) 

driver.close()  
print("Its Done")
