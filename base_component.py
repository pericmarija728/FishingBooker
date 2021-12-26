import selenium.webdriver as webdriver
from selenium.webdriver.remote.webelement import WebElement
from abc import ABC

class BaseComponent(ABC):
    driver: webdriver
    element: WebElement

    def __init__(self, driver: webdriver, element: WebElement):
        self.driver = driver
        self.element = element