import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
options_obj=webdriver.ChromeOptions()
options_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options_obj)

# driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
# #driver.maximize_window()
#
# a=driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
# print(a)
# driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']").click()
# b=driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
# print(b)

driver.get("https://www.yatra.com/hotels")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@id='BE_Hotel_pax_info']//i").click()
(driver.find_element(By.XPATH,"//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]")
 .click())
