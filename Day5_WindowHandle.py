import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
options_obj=webdriver.ChromeOptions()
options_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
a=driver.current_window_handle
print(a)
time.sleep(5)
title1=driver.title
print(title1)
#Human Resources Management Software | OrangeHRM
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

all_handles=driver.window_handles
for i in all_handles:
    driver.switch_to.window(i)
    if driver.title=="Human Resources Management Software | OrangeHRM":
        driver.close()




#all_handles=driver.window_handles
#print(all_handles)
# for i in all_handles:
#     if i != a:
#         driver.switch_to.window(i)
#         time.sleep(5)
#         driver.find_element(By.XPATH,"//a[normalize-space()='Company']").click()
#         driver.close()
#         #driver.find_element(By.LINK_TEXT,"Company").click()
#
# driver.switch_to.window(a)
# driver.find_element(By.NAME,"username").send_keys("admin123")
# time.sleep(5)
# driver.close()




