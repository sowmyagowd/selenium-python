import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj=Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
options_obj=webdriver.ChromeOptions()
options_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
time.sleep(4)

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
driver.find_element(By.ID,"datepicker").click()
time.sleep(4)
#driver.find_element(By.ID,"datepicker").send_keys("06/11/2024")
# driver.find_element(By.XPATH,"//span[normalize-space()='Next']").click()
# driver.find_element(By.XPATH,"//span[normalize-space()='Prev']").click()

year="2023"
month="May"
Day="16"

while 1:
    mnt=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if mnt==month and yr==year:
        break
    else:
        #driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Prev']").click()
#select date:
a=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//td")
for i in a:
    print(i.text)
    if i.text==Day:
        i.click()


