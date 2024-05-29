from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
options_obj=webdriver.ChromeOptions()
options_obj.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj,options=options_obj)

#driver.get("https://demo.nopcommerce.com/")
#driver.maximize_window()
#print(driver.title)
# driver.find_element(By.NAME,"q").send_keys("phone")
# driver.find_element(By.XPATH,"//button[normalize-space()='Search']").click()
# exp_title="nopCommerce demo store. Search"
# act_title=driver.title
# if exp_title==act_title:
#     print("pass")
# else:
#     print("fail")

#driver.find_element(By.LINK_TEXT,"Register").click()
#count= driver.find_elements(By.LINK_TEXT,"Register")   #this is wrong find elements will work
#print(len(count))   # this is wrong

#driver.find_element(By.PARTIAL_LINK_TEXT,"gister").click()

#link=driver.find_elements(By.TAG_NAME,"a")
#print(len(link))

#driver.find_element(By.CLASS_NAME,"answer").click()
#print(len(a))
#print(a[0].text)

#for i in a:
 #   print(i.text)

#b=driver.find_elements(By.TAG_NAME,"li")
#print(len(b))
# print(b[2].text)

driver.get("https://www.facebook.com")
driver.title
driver.maximize_window()


driver.close()






