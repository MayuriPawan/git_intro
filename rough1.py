from time import sleep
from selenium.webdriver import Chrome

driver = Chrome(r"C:\WORKSPACE\_SELENIUM\DATAFILES\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.flipkart.com/")
sleep(2)
driver.find_element("xpath", "//button[text()='✕']").click()
driver.find_element("name", "q").send_keys("girls shoes")
driver.find_element("class name", "L0Z3Pu").click()
sleep(2)
element = driver.find_element("xpath","(//div[text()='Miss & Chief']/..//span)[1]").text
print(f"discount on Miss & Chief shoues is {element}")
driver.minimize_window()