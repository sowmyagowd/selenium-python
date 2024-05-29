from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj=Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
options_obj=webdriver.ChromeOptions()
options_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
#count Rows
rows=driver.find_elements(By.XPATH,"//table[@id='productTable']//tr")
print(len(rows))
#count columns
col=driver.find_elements(By.XPATH,"//table[@id='productTable']//th")
print(len(col))

# data=driver.find_elements(By.XPATH,"//table[@id='productTable']//td")
# for i in data:
#     if (i.text)=="Product3":
#         print("item found")
#         break
#     else:
#         print("not found")

# read all data
# data=driver.find_elements(By.XPATH,"//table[@id='productTable']//td")
# for i in data:
#     print(i.text)

# Approach2: Read all data
# for i in range(2,len(rows)):
#     for j in range(1,len(col)):
#         a=driver.find_element(By.XPATH,"//table[@id='productTable']//tr["+str(i)+"]/td["+str(j)+"]").text
#         print(a)
#     print("   ")

#Read column
for i in range(1,len(rows)):
    data=driver.find_element(By.XPATH,"//table[@id='productTable']//tr["+str(i)+"]/td[2]").text
    if data=="Product 3":
        driver.find_element(By.XPATH,"//table[@id='productTable']//tr["+str(i)+"]/td[4]/input").click()



#driver.find_element(By.XPATH,"//table[@id='productTable']//tr[3]/td[4]/input").click()
#driver.find_element(By.XPATH,"//*[@id='productTable']/tbody/tr[3]/td[4]/input").click()












