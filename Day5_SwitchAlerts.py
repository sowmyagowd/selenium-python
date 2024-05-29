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

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']").click()
#driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()

time.sleep(5)
driver.switch_to.alert.send_keys("hello selenium")
driver.switch_to.alert.accept()
#driver.switch_to.alert.dismiss()

