from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("C:\WORKSPACE\_SELENIUM\DATAFILES\chromedriver.exe")
driver.get("https://www.facebook.com/")

driver.maximize_window()
driver.find_element_by_id("email").send_keys("123@gmail.com")
sleep(2)
driver.find_element_by_id("pass").send_keys("123123")
sleep(3)
driver.find_element_by_name("login").click()
sleep(2)
driver.close()


