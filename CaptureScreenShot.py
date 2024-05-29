import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
options_obj=webdriver.ChromeOptions()
options_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options_obj)

driver.get("https://secure.yatra.com/social/common/yatra/register")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[@id='login-continue-btn']").click()
#driver.save_screenshot(".\\test.png")
#driver.save_screenshot("C:\\Drivers\\error.png")
#driver.get_screenshot_as_file("C:\\Drivers\\error.png")
#driver.get_screenshot_as_file(".\\test123.png")

