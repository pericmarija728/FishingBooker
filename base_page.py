import selenium.webdriver as webdriver
from abc import ABC

class BasePage(ABC):
     driver : webdriver

     def __init__(self, driver : webdriver):
        self.driver = driver
