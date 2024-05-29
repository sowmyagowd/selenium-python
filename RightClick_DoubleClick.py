import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
options_obj=webdriver.ChromeOptions()
options_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options_obj)

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
                     #double Click
act=ActionChains(driver)
act.double_click(driver.find_element(By.XPATH,"//button[normalize-space()='Double-Click Me To See Alert']")).perform()
time.sleep(2)
driver.switch_to.alert.accept()

                     #right Click
right_ele=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
act.context_click(right_ele).perform()
time.sleep(2)

driver.find_element(By.XPATH,"//li[@class='context-menu-item context-menu-icon context-menu-icon-copy']").click()