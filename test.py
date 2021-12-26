import datetime
import selenium.webdriver as webdriver
from booking_page import BookingPage


base_url = 'https://fishingbooker:QAFBTest@qahiring.dev.fishingbooker.com/charters/view/22879'

def test():
    drv = webdriver.Chrome()
    drv.maximize_window()
    drv.get(base_url)
    booking_page = BookingPage(drv)
    details_page = booking_page.search(datetime.datetime(2022, 1, 1), datetime.datetime(2022, 6, 30), "Single Fisherman Special")
    payment_page = details_page.enter_details("Marija", "Jankovic", "janko.marija@yahoo.com", "2244", "Hello captain Aleksandar!")
    final_page = payment_page.confirm_booking("4111111111111111", "07/2022", "224", "Marija Jankovic", "224", "United States")
    booking_number = final_page.read_booking_number()
    file = open(f"{booking_number}.txt", "x")
    file.write(booking_number)
    assert True

if __name__ == "__main__":
    test()