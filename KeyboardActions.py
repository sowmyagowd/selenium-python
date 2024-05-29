import time

from selenium import webdriver
from selenium.webdriver import Keys
#from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
options_obj=webdriver.ChromeOptions()
options_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options_obj)

# driver.get("https://www.facebook.com/")
# driver.maximize_window()
#
# time.sleep(5)
#
# act=ActionChains(driver)
# act.send_keys(Keys.ENTER).perform()


# driver.find_element(By.XPATH,"//input[@id='email']").send_keys("Sowmya")
# act=ActionChains(driver)
# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL).perform()
#
# act.key_down(Keys.CONTROL)
# act.send_keys("c")
# act.key_up(Keys.CONTROL).perform()
#
# act.send_keys(Keys.TAB).perform()
#
# act.key_down(Keys.CONTROL)
# act.send_keys("v")
# act.key_up(Keys.CONTROL).perform()

# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window("tab")
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#
# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window("window")
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.get("https://www.facebook.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='email']").send_keys("Sowmya")



