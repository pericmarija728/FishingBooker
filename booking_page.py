import datetime
from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datepicker import Datepicker
from details_page import DetailsPage, DetailsLocators

class BookingPage(BasePage):
     
      def search(self, start_date: datetime.datetime, end_date: datetime.datetime, package_name: str) -> DetailsPage:
            ActionChains(self.driver).move_to_element(self.driver.find_element(*BookingPageLocators.first_item)).perform()
            self.driver.find_element(*BookingPageLocators.days).click()
            self.driver.find_element(*BookingPageLocators.one_days).click()
            self.driver.find_element(*BookingPageLocators.group_size).click()
            self.driver.find_element(*BookingPageLocators.adults).click()
            self.driver.find_element(*BookingPageLocators.children).click()
            datepicker = Datepicker(self.driver, self.driver.find_element(*BookingPageLocators.trip_date))
            while start_date <= end_date:
                  if datepicker.set_date(start_date) == False:
                        start_date = start_date + datetime.timedelta(days=1)
                        continue
                  self.driver.find_element(*BookingPageLocators.check_availability_button).click()
                  WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(BookingPageLocators.change_search_button))
                  packages = self.driver.find_elements(*BookingPageLocators.charter_package)
                  package = list(filter(lambda x: str.lower(x.find_element(*BookingPageLocators.charter_package_title).text.strip()) == str.lower(package_name), packages))[0]
                  package_button = package.find_element(*BookingPageLocators.charter_package_button)
                  if "bookbtn" not in package_button.get_attribute('id'):
                        start_date = start_date + datetime.timedelta(days=1)
                        continue
                  package_button.click()
                  WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(DetailsLocators.details_section))
                  break
            else:
                  raise ValueError("There are no available dates in provided range")
            return DetailsPage(self.driver)
        
class BookingPageLocators:

      first_item = (By.CSS_SELECTOR, "#packages-container > div.charter-packages-container.clearfix > ul > div > li:nth-child(1)")
      trip_date = (By.ID, "booking_date_availability_form_search")
      days = (By.ID,"booking_days")
      one_days = (By.CSS_SELECTOR, "#booking_days > option:nth-child(1)")
      group_size = (By.CSS_SELECTOR,"#charter-trips > div.packages-outer-container.without-date > div > div.persons.availability-form-persons.col-xs-12 > div.search-form-persons > input.search-booking-persons.fbkr-input.gray.search-form-input.arrow")
      adults = (By.CSS_SELECTOR, "#charter-trips > div.packages-outer-container.without-date > div > div.persons.availability-form-persons.col-xs-12 > div.search-form-persons > div > table:nth-child(1) > tbody > tr > td:nth-child(2) > table > tbody > tr > td:nth-child(1) > button")
      children = (By.CSS_SELECTOR, "#charter-trips > div.packages-outer-container.without-date > div > div.persons.availability-form-persons.col-xs-12 > div.search-form-persons > div > table.row-space-top-3 > tbody > tr > td:nth-child(2) > table > tbody > tr > td.text-right > button")
      check_availability_button = (By.ID,"check-availability-btn")
      change_search_button = (By.ID, "change-search-btn")
      charter_package = (By.CSS_SELECTOR, "#packages-container .charter-packages-container .package-item")
      charter_package_title = (By.CSS_SELECTOR, ".package-title")
      charter_package_button = (By.CSS_SELECTOR, "button[name='booking_package']")