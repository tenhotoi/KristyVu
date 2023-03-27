# https://www.numpyninja.com/post/difference-between-x-path-and-css-selector-in-selenium

"""
Selenium is an open source, automated, and valuable tool used for test automation.  However, Selenium is not just a single tool but a collection of tools. It provides a single interface that lets you write test scripts in programming languages like Ruby, Java, NodeJS, PHP, Pearl, Python, and C#, among others. It works with all types of browsers and operating systems.

Selenium Tools Suite

---Selenium Integrated Development Environment (IDE)

---Selenium Remote Control (RC)

---WebDriver

---Selenium Grid

 In order to perform automation testing, we would need to locate HTML elements. 
 We can locate these web elements using either X-path or CSS selectors. 
 This article will address the various differences between XPath and CSS selectors. 
 Along the way, we’ll talk about what each of the options brings to the table.
"""


# https://www.tutorialspoint.com/what-are-the-differences-between-xpath-and-css-in-selenium-with-python

"""
Both xpath and css are one the most frequently used locators in Selenium. Though there are other locators like id, name, classname, tagname, and link text and so on, xpath and css are used when there are no unique attributes available to identify the elements.

There are some differences between xpath and css listed below −

Xpath allows bidirectional flow which means the traversal can be both ways from parent to child and child to parent as well. Css allows only one directional flow which means the traversal is from parent to child only.

Xpath is slower in terms of performance and speed. Css has better performance and speed than xpath.

Xpath allows identification with the help of visible text appearing on screen with the help of text() function. Css does not have this feature.

Customized css can be created directly with the help of attributes id and class. For id, the css expression is represented by # followed by the id [ #<<id expression>>. For class, the css expression is represented by . followed by the class [.<<class expression>>]. Xpath does not have any feature like this.

Xpath expression is represented by [//tagname[@attribute = 'value']. The css expression is repression is represented by [tagname[attribute = 'value'].

There are two types of xpath – absolute and relative. But css has no such types.

Example
Code Implementation with css.
"""

from selenium import webdriver
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://www.tutorialspoint.com/index.htm")
#to refresh the browser
driver.refresh()
# identifying the edit box with the help of css driver. 
elements = driver.find_element_by_css_selector("input[class='gsc-input']")
elements.send_keys("Selenium")  # https://www.geeksforgeeks.org/send_keys-element-method-selenium-python/
#to close the browser
driver.close()

"""
Code Implementation with xpath
"""
from selenium import webdriver
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke actual browser
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://www.tutorialspoint.com/index.htm")
#to refresh the browser
driver.refresh()
# identifying the edit box with the help of xpath
elements = driver.find_element_by_xpath("//input[@class='gsc-input']")
elements.send_keys("Selenium")  # https://www.geeksforgeeks.org/send_keys-element-method-selenium-python/
#to close the browser
driver.close()