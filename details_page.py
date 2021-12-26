from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from payment_page import PaymentPage, PaymentPageLocators

class DetailsPage(BasePage):

    def enter_details(self, first_name, last_name,email_address, mobile_number, sey_hello) -> PaymentPage:
        self.driver.find_element(*DetailsLocators.first_name).send_keys(first_name)
        self.driver.find_element(*DetailsLocators.last_name).send_keys(last_name)
        self.driver.find_element(*DetailsLocators.email_address).send_keys(email_address)
        self.driver.find_element(*DetailsLocators.mobile_number).send_keys(mobile_number)
        ActionChains(self.driver).move_to_element(self.driver.find_element(*DetailsLocators.continue_butoon)).perform()  
        self.driver.find_element(*DetailsLocators.sey_hello).send_keys(sey_hello)
        self.driver.find_element(*DetailsLocators.continue_butoon).click()
        WebDriverWait(self.driver, 30).until(EC.frame_to_be_available_and_switch_to_it(PaymentPageLocators.card_number_frame))
        return PaymentPage(self.driver)
        

class DetailsLocators:
    details_section = (By.ID, "your-details-section")
    first_name = (By.CSS_SELECTOR, "input[data-testid='checkout-first-name-input']")
    last_name = (By.CSS_SELECTOR, "input[data-testid='checkout-last-name-input']" )
    email_address = (By.CSS_SELECTOR,"input[data-testid='checkout-email-input']")
    mobile_number = (By.CSS_SELECTOR, "input[type='tel']")
    sey_hello = (By.CSS_SELECTOR, "textarea[data-testid='special-requests-textarea']" )
    continue_butoon = (By.CSS_SELECTOR, "#checkout-v2 button[type='submit']")