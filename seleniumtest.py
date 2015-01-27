#!/usr/bin/env python

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import sys, os
from traceback import print_exception
from time import sleep

def describe():
   for el in driver.find_elements_by_tag_name("body"):
      if el.is_displayed():
         print el.text

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

def ctrl_click(element):
   chain = webdriver.ActionChains(driver)
   chain.key_down(Keys.CONTROL)
   chain.click(element)
   chain.key_up(Keys.CONTROL)
   chain.perform()

def accept_alert():
   Alert(driver).accept()

def quit():
   describe()
   driver.quit()
   os.listdir("testoverview_javascript") # Seems to be required for the comment files to be found later on...

class LookupDir(dict):
   def __getitem__(self, key):
      globDict = globals()
      if key in globDict:
         return globDict[key]
      elif hasattr(driver, key):
         return getattr(driver, key)
      elif hasattr(__builtins__, key):
         return getattr(__builtins__, key)
      else:
         return self.getElement(key)

   def getElement(self, key):
      for _ in range(10):
         try:
            return driver.find_element_by_id(key)
         except NoSuchElementException:
            sleep(0.5)
   

try:
   localTmp = os.path.dirname(os.getenv("TEXTTEST_SANDBOX_ROOT"))
   filename = os.path.join(os.getenv("TEXTTEST_SANDBOX"), "overview.html")
   url = filename.replace(localTmp, os.getenv("TEXTTEST_LOCAL_TMP_URL"))
   driver.get(url)
   usecase = os.path.abspath("usecase.py")
   execfile(usecase, LookupDir())
except:
   type, value, traceback = sys.exc_info()
   print_exception(type, value, traceback)
   driver.quit()
