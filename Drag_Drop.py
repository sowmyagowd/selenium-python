import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
options_obj=webdriver.ChromeOptions()
options_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options_obj)

# driver.get("https://jqueryui.com/droppable/")
# driver.maximize_window()

# driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
# drag=driver.find_element(By.ID,"draggable")
# drop=driver.find_element(By.ID,"droppable")
# act= ActionChains(driver)
# act.drag_and_drop(drag,drop).perform()

              #### Drag and drop By Offset
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

time.sleep(4)

min=driver.find_element(By.XPATH,"//div[@id='slider-range']//span[1]")
max=driver.find_element(By.XPATH,"//div[@id='slider-range']//span[2]")

# print(min)  59 250
# print(max) 612 250

act=ActionChains(driver)
act.drag_and_drop_by_offset(min,40,300).perform()

