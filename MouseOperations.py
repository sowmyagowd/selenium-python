import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj=Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
options_obj=webdriver.ChromeOptions()
options_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options_obj)

driver.get("https://www.yatra.com/")
driver.maximize_window()
time.sleep(4)

#go to Move---> click on trains
my_acc=driver.find_element(By.XPATH,"//a[contains(text(),'My Account')]")
act=ActionChains(driver)
act.move_to_element(my_acc).perform()
time.sleep(4)
driver.find_element(By.XPATH,"//a[@title='My Bookings']").click()


# act.move_to_element(driver.find_element(By.XPATH,"//span[@class='more-arr']")).perform()
# time.sleep(4)
# driver.find_element(By.XPATH,"//span[normalize-space()='Trains']").click()
