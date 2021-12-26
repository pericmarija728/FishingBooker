from base_page import BasePage
from final_page import FinalPage, FinalPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class PaymentPage(BasePage):

    def confirm_booking(self, card_number, expiration_date, security_code, name_on_card, postal_code, country) -> FinalPage:
        self.driver.find_element(*PaymentPageLocators.card_number).send_keys(card_number)
        
        self.driver.switch_to.default_content()
        iframe_expiration = self.driver.find_element(*PaymentPageLocators.expiration_date_frame)
        self.driver.switch_to.frame(iframe_expiration)
        self.driver.find_element(*PaymentPageLocators.expiration_date).send_keys(expiration_date)
        
        self.driver.switch_to.default_content()
        iframe_cvv = self.driver.find_element(*PaymentPageLocators.security_code_frame)
        self.driver.switch_to.frame(iframe_cvv)
        self.driver.find_element(*PaymentPageLocators.security_code).send_keys(security_code)

        self.driver.switch_to.default_content()
        iframe_name = self.driver.find_element(*PaymentPageLocators.name_on_card_frame)
        self.driver.switch_to.frame(iframe_name)
        self.driver.find_element(*PaymentPageLocators.name_on_card).send_keys(name_on_card)

        self.driver.switch_to.default_content()
        Select(self.driver.find_element(*PaymentPageLocators.billing_country)).select_by_visible_text(country)

        iframe_zip = self.driver.find_element(*PaymentPageLocators.postal_code_frame)
        self.driver.switch_to.frame(iframe_zip)
        self.driver.find_element(*PaymentPageLocators.postal_code).send_keys(postal_code)

        self.driver.switch_to.default_content()
        ActionChains(self.driver).move_to_element(self.driver.find_element(*PaymentPageLocators.confirm_booking_button)).perform()
        self.driver.find_element(*PaymentPageLocators.confirm_booking_button).click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(FinalPageLocators.booking_number))
        return FinalPage(self.driver)
        
class PaymentPageLocators:
    card_number_frame = (By.ID, "braintree-hosted-field-number")
    card_number = (By.ID, "credit-card-number")
    expiration_date_frame = (By.ID, "braintree-hosted-field-expirationDate")
    expiration_date = (By.ID, "expiration")
    security_code_frame = (By.ID, "braintree-hosted-field-cvv")
    security_code = (By.ID, "cvv")
    name_on_card_frame = (By.ID, "braintree-hosted-field-cardholderName")
    name_on_card = (By.ID,"cardholder-name")
    billing_country = (By.CSS_SELECTOR, "select[data-testid='checkout-billing-country-select']")
    postal_code_frame = (By.ID, "braintree-hosted-field-postalCode")
    postal_code = (By.ID, "postal-code")
    confirm_booking_button = (By.CSS_SELECTOR, "#checkout-v2 button[type='submit']")


