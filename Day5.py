import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj=Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
options_obj=webdriver.ChromeOptions()
options_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options_obj)

#driver.get("https://demo.nopcommerce.com/")
#driver.maximize_window()
#driver.implicitly_wait(5)

#       Click on link
#driver.find_element(By.LINK_TEXT,"Digital downloads").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

#   total number of links in a page
#a=driver.find_elements(By.TAG_NAME,"a")
#print(len(a))
#a=driver.find_elements(By.XPATH,"//a")
#print(len(a))

#for i in a:
 #   print(i.text)

          ################## Broken Links ##################

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
driver.implicitly_wait(10)
a=driver.find_elements(By.TAG_NAME,"a")
print(len(a))

count=0
valid=0
for i in a:
    url=i.get_attribute("href")
    try:
        res=requests.head(url)

    except:
        None

    if res.status_code>=400:

        count=count+1
    else:

        valid=valid+1
print("total of valid link",valid)
print("total of broken link",count)
driver.close()