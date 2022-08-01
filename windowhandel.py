'''
launch demowebshop.
click “Twitter” link at the footer of
the webpage.
”twitter” webpage opens in a new
tab.
get window handles and switch to
twitter tab and enter some text in
search field
switch back to parent window and
click on “Register” link
'''


from selenium.webdriver import Chrome
from time import sleep

driver = Chrome("C:\WORKSPACE\_SELENIUM\DATAFILES\chromedriver.exe")
driver.maximize_window()
driver.get('http://demowebshop.tricentis.com/')

driver.find_element("xpath", "//a[text()='Twitter']").click()
sleep(3)
handles = driver.window_handles
driver.switch_to.window(handles[1])
sleep(5)
# driver.switch_to_frame(1)
# driver.find_element("id", "close").click()
driver.find_element_by_xpath("//input[@placeholder='Search Twitter']").send_keys("hello")
sleep(5)
driver.switch_to.window(handles[0])
sleep(4)
driver.find_element("xpath", "//a[text()='Register']").click()
sleep(3)
driver.minimize_window()
sleep(3)
driver.quit()



