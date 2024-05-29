import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
options_obj=webdriver.ChromeOptions()
options_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options_obj)


#driver.get("https://www.facebook.com")
# driver.get("https://demo.nopcommerce.com/")
# print(driver.title)
# driver.maximize_window()
#
# a=driver.find_element(By.XPATH,"//a[normalize-space()='Register']").is_displayed()
# print(a)
# driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()
#
# driver.find_element(By.XPATH,"//input[@id='gender-female']").click()
#
# b=driver.find_element(By.XPATH,"//input[@id='gender-female']").is_selected()
#print(b)
# driver.close()



#/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a
#driver.find_element(By.XPATH,"//input[@id='small-searchterms']").send_keys("phone")
#driver.find_element(By.XPATH,"//input[@name='email' or @data-testid='royal_email']").send_keys("sowmya")

#driver.find_element(By.LINK_TEXT,"Forgot password?").click()
#driver.find_element(By.XPATH,"//a[text()='Forgot password?']").click()
# driver.find_element(By.XPATH,"//a[normalize-space()='Forgot password?']").click()
#driver.find_element(By.XPATH,"//input[contains(@placeholder,'Search')]").send_keys("phone")
#a=driver.find_element(By.XPATH,"//button[starts-with(@type,'sub')]").text
#print(a)

#driver.find_element(By.XPATH,"//input[contains(@data-testid,'royal_ema')]").send_keys("sowmya")

#driver.close()


######  get commands means getting the information of the page, URL title etc




#inputtext _55r1 _6luy


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
time.sleep(5)
driver.refresh()