#!/users/dgalda/.local/python2.6.current/bin/python

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
import time, sys, os

def writeTableLines(filename):
   with open(filename, 'w') as f1:
      elements0 = driver.find_elements_by_tag_name("TR")
      for el in elements0:
         f1.write( el.text + '\n')
   

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

filename = os.path.abspath("overview.html")

driver.get("file://" + filename)
writeTableLines('f1.txt')

for line in sys.stdin:
    if len(line.strip()) > 0:
        element1 = driver.find_element_by_id(line.strip())
        element1.click()

time.sleep(3)
writeTableLines('f2.txt')

try:
    #WebDriverWait(driver, 10).until(lambda driver : driver.title.lower().startswith("cheese!"))

    print driver.title

finally:
    driver.quit()
