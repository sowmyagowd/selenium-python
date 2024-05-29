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


driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

drop_down=Select(driver.find_element(By.XPATH,"//select[contains(@id,'drop')]"))
#drop_down.select_by_visible_text("doc 1")
#drop_down.select_by_value("mno")
#drop_down.select_by_index(2)
lists=drop_down.options

for i in lists:
    print(i.text)




