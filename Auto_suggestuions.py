import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
options_obj=webdriver.ChromeOptions()
options_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options_obj)

driver.get("https://www.yatra.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']").click()
driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']").send_keys("New Delhi")
driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']").send_keys(Keys.ENTER)
time.sleep(4)

driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']").send_keys("New")
a=driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
print(len(a))

# for i in a:
#     if "New York (JFK)" in i.text:
#         i.click()
#         break

for i in a:
    if "New York (JFK)" in i.text:
        i.click()
        break