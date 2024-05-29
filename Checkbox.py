from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj=Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
options_obj=webdriver.ChromeOptions()
options_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options_obj)

driver.implicitly_wait(10)
driver.get("https://omayo.blogspot.com/")
driver.title
driver.maximize_window()

chk_box=driver.find_elements(By.XPATH,"//input[@type='checkbox' and @name='accessories']")
print(len(chk_box))

for i in chk_box:
    if i.get_attribute('value')=="Bag" or i.get_attribute("value")=="Laptop":
        i.click()


# a=driver.find_element(By.XPATH,"//a[normalize-space()='Non Stop Flights']").is_selected()
# print(a)
# if a==False:
#     driver.find_element(By.XPATH,"//a[normalize-space()='Non Stop Flights']").click()

#count number of checkboxes:
# check_box=driver.find_elements(By.XPATH,"//div[@class='search-filter flex-search-filter']//a")
# print(len(check_box))

#for i in check_box:
#    i.click()

# for i in range(len(check_box)):
#     check_box[i].click()





