import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from base_component import BaseComponent

class Datepicker(BaseComponent):
    def set_date(self, date: datetime.datetime) -> bool:
        month = str.lower(date.strftime("%B"))
        year = date.year
        day = date.day
        self.element.click()
        ActionChains(self.driver).move_to_element(self.driver.find_element(*DatepickerSelectors.datepicker_container)).perform()
        current_date = self.driver.find_element(*DatepickerSelectors.datepicker_switch).text.strip().split()
        current_month = str.lower(current_date[0])
        current_year = str.lower(current_date[1])
        while month != current_month or str(year) != current_year:
            self.driver.find_element(*DatepickerSelectors.next_button).click()
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(DatepickerSelectors.next_button))
            current_date = self.driver.find_element(*DatepickerSelectors.datepicker_switch).text.strip().split()
            current_month = str.lower(current_date[0])
            current_year = str.lower(current_date[1])
        days = self.driver.find_elements(*DatepickerSelectors.day)
        day_to_select = list(filter(lambda x: x.text.strip() == str(day) and self.is_available_day(x), days))
        if len(day_to_select) < 1:
            return False
        day_to_select[0].click()
        return True
        
    def is_available_day(self, element: WebElement) -> bool:
        classes = element.get_attribute('class').strip().split()
        if 'old' in classes or 'new' in classes or 'disabled' in classes:
            return False
        return True

class DatepickerSelectors:
    datepicker_container = (By.CSS_SELECTOR, ".datepicker")
    next_button = (By.CSS_SELECTOR, ".datepicker .datepicker-days .next")
    datepicker_switch = (By.CSS_SELECTOR, ".datepicker .datepicker-days .datepicker-switch")
    day = (By.CSS_SELECTOR, ".datepicker .datepicker-days .day")