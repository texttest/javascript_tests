#!/users/dgalda/.local/python2.6.current/bin/python

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
import time, sys, os

def writeTableLines():
   elements0 = driver.find_elements_by_tag_name("TR")
   for el in elements0:
      if el.is_displayed():
         print el.text
   

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

try:
    filename = os.path.abspath("overview.html")

    driver.get("file://" + filename)
    
    for unstrippedLine in sys.stdin:
        line = unstrippedLine.strip()
        if len(line) > 0:
            elementId = line.split(':')[0]
            action = line.split(':')[1]
            element = driver.find_element_by_id(elementId)
            eval("element." + action)

    time.sleep(1)
    writeTableLines()
    
    #WebDriverWait(driver, 10).until(lambda driver : driver.title.lower().startswith("cheese!"))

    #print driver.title

finally:
    driver.quit()
