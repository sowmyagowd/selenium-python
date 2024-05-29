import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj=Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
options_obj=webdriver.ChromeOptions()
options_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options_obj)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
driver.implicitly_wait(10)

driver.execute_script("window.scrollBy(0,3000)","")
value=driver.execute_script("return window.pageYOffset;")
print(value)

#approach2
# mywait=WebDriverWait(driver,10)
# flag=mywait.until(EC.presence_of_element_located((By.XPATH,"//img[@alt='Flag of India']")))
# driver.implicitly_wait(10)
# flag =driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)