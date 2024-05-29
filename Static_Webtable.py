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

rows=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
print(len(rows))

columns=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/th")
print(len(columns))
#
# a=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/td[2]")
#
# for i in a:
#     print(i.text)
#
# b=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[2]")
# for i in b:
#     print(i.text)

# a=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[2]/td[3]")
# print(a.text)


# count=0
# for i in rows:
#     if i.text=="Selenium":
#         count=count+1
# print(count)
# print("pass")

# Read all rows and columns
# all_data=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/td")
# for i in all_data:
#     print(i.text)

#Approach 2: read all data

# for i in range(2,len(rows)+1):
#     for j in range(1,len(columns)+1):
#         data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
#         print(data)
#     print("  ")

## list book names whose author name is mukesh

for i in range(2,len(rows)+1):
    author=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(i)+"]//td[2]").text
    if author=="Mukesh":
        book_name=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(i)+"]//td[1]").text
        print(book_name)




driver.close()




        