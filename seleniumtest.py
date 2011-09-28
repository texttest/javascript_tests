#!/users/dgalda/.local/python2.6.current/bin/python

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
import time, sys, os

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

filename = os.path.abspath("overview.html")

driver.get("file://" + filename)
with open('f1.txt', 'w') as f1:
   elements0 = driver.find_elements_by_tag_name("TR")
   for el in elements0:
      f1.write( el.text + '\n')

for line in sys.stdin:
    if len(line.strip()) > 0:
        element1 = driver.find_element_by_id(line.strip())
        element1.click()

with open('f2.txt', 'w') as f2:
   elements = driver.find_elements_by_tag_name("TR")
   for e in elements:
      f2.write( e.text + '\n')

try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    #WebDriverWait(driver, 10).until(lambda driver : driver.title.lower().startswith("cheese!"))

    print driver.title

finally:
    driver.quit()
