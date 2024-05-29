from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
options_obj=webdriver.ChromeOptions()
options_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options_obj)


driver.get("https://www.facebook.com")
driver.title
driver.maximize_window()

## Tag#id,    Tag.Class,   Tag[attribute],     Tag.Class[attribute]
##Customised locator

#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("sowmyagowda.hsn@gmail.com")
#driver.find_element(By.CSS_SELECTOR,"#email").send_keys("sowmya")
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("Ilovehassan8")

#driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("sowmya")

driver.find_element(By.CSS_SELECTOR,".inputtext[data-testid=royal_email]").send_keys("sowmyagowda.hsn@gmail.com")
driver.find_element(By.CSS_SELECTOR,".inputtext[placeholder=Password]").send_keys("Ilovehassan8")

