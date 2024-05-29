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

#driver.get("https://testautomationpractice.blogspot.com/")
#driver.get("https://www.redbus.com/")
# driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
# driver.maximize_window()

# driver.find_element(By.XPATH,"//div[@class='rdc-login']").click()
# driver.find_element(By.XPATH,"//li[@id='signInLink']").click()
# driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='modalIframe']"))
# driver.find_element(By.XPATH,"//span[normalize-space()='Sign in with Google']").click()

#An iframe with a thin black border:
#driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[normalize_space='An iframe with a thin black border:']"))
#driver.find_element(By.XPATH,"//a[@id='navbtn_tutorials']").click()


driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
#driver.find_element(By.XPATH,"//input[@id='name']").send_keys("sowmya")

driver.switch_to.frame("frame-one796456169")
driver.find_element(By.XPATH,"//input[@id='RESULT_TextField-0']").send_keys("hello")
time.sleep(5)

drop_down=Select(driver.find_element(By.XPATH,"//select[@class='drop_down' and @id='RESULT_RadioButton-3']"))
drop_down.select_by_visible_text("QA Engineer")

driver.switch_to.parent_frame()
#driver.switch_to.default_content()
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("sowmya")

# driver.get("https://demo.automationtesting.in/Frames.html")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()
# driver.switch_to.frame(driver.find_element(By.XPATH,"//*[@id='Multiple']/iframe"))
# driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@src='SingleFrame.html']"))
# driver.find_element(By.XPATH,"//input[@type='text']").send_keys("welcome Selenium")

