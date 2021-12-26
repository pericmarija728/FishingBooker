from base_page import BasePage
from selenium.webdriver.common.by import By

class FinalPage(BasePage):
    def read_booking_number(self) -> str:
        return self.driver.find_element(*FinalPageLocators.booking_number).text.strip().rstrip('.')

class FinalPageLocators:
    booking_number = (By.CSS_SELECTOR, "strong[data-testid='booking-id']")