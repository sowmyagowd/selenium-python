import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj=Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
options_obj=webdriver.ChromeOptions()
options_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

#click on DOB
driver.find_element(By.XPATH,"//input[@id='dob']").click()

mn="Feb"
yr="2022"
#select month
month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
month.select_by_visible_text(mn)

year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
year.select_by_visible_text(yr)

date=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody/tr/td/a")
for i in date:
    if(i.text)=="10":
        i.click()
        break