from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")

obj_options=webdriver.ChromeOptions()
obj_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=obj_options)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
print(driver.title)

time.sleep(5)
driver.find_element(By.NAME,"username").send_keys("admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,value="//button[normalize-space()='Login']").click()

expected_title="OrangeHRM"
actual_title= driver.title
print(actual_title)
if actual_title==expected_title:
    print("pass")
else:
    print("fail")
driver.close()