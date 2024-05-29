from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj=Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
options_obj=webdriver.ChromeOptions()
options_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options_obj)


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.title
driver.maximize_window()

mywait=WebDriverWait(driver,10)
mywait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Username']"))).send_keys("admin")
mywait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Password']"))).send_keys("admin123")
mywait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Login']"))).click()


