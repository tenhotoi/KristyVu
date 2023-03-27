# https://www.geeksforgeeks.org/implicit-waits-in-selenium-python/
# https://www.geeksforgeeks.org/waits-in-selenium-python/?ref=rp
# 1. Implicit Waits in Selenium Python
# import webdriver 
from selenium import webdriver 
  
# create webdriver object 
driver = webdriver.Firefox() 
    
# set implicit wait time
driver.implicitly_wait(10) # seconds
  
# get geeksforgeeks.org 
driver.get("https://www.geeksforgeeks.org/") 
    
# get element after 10 seconds
element = driver.find_element_by_link_text("Courses")
  
# click element
element.click()

# https://www.geeksforgeeks.org/explicit-waits-in-selenium-python/?ref=rp
# 2. Explicit waits in Selenium Python
"""
This waits up to 10 seconds before throwing a TimeoutException unless it finds the element to return within 10 seconds. WebDriverWait by default calls the ExpectedCondition every 500 milliseconds until it returns successfully.
"""
# import necessary classes
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create driver object
driver = webdriver.Firefox()

# A URL that delays loading
driver.get("http://somedomain / url_that_delays_loading")

try:
	# wait 10 seconds before looking for element
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, "myDynamicElement"))
	)
finally:
	# else quit
	driver.quit()
