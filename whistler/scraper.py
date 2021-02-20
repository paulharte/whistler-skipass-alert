from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from whistler.chromeWebdriver import make_driver
from whistler.utils import sanitise_month_name

WHISTLER_AVAILABILITY_PAGE = "https://www.whistlerblackcomb.com/plan-your-trip/lift-access/check-availability.aspx"


class WhistlerScraper(object):
    def __init__(self, headless=True):
        self.driver = make_driver(headless)
        self.driver.maximize_window()
        self.driver.get(WHISTLER_AVAILABILITY_PAGE)
        self.click_availability_button()

    def __del__(self):
        if hasattr(self, "driver") and self.driver:
            self.driver.close()
            self.driver.quit()

    def click_availability_button(self):
        self.driver.execute_script("window.scrollTo(0, 550)")
        button_id = "passHolderReservationsSearchButton"
        WebDriverWait(self.driver, 8).until(
            EC.element_to_be_clickable((By.ID, button_id))
        )
        check_availability = self.driver.find_element_by_id(button_id)
        check_availability.click()

        WebDriverWait(self.driver, 8).until(
            EC.visibility_of_any_elements_located(
                (By.CSS_SELECTOR, ".capacity_calendar__month")
            )
        )

    def check_day_is_open(self, day: int, month: str) -> bool:
        month = sanitise_month_name(month)
        calendar = self.driver.find_element_by_class_name("capacity_calendar")
        month_header = calendar.find_element_by_xpath(
            ".//*[contains(text(), '%s')]" % month
        )
        month_element = month_header.find_element_by_xpath(
            ".//ancestor::div[@class='capacity_calendar__month']"
        )
        day_grid = month_element.find_element_by_class_name(
            "capacity_calendar__month__days"
        )
        day_element = day_grid.find_element_by_xpath(
            ".//span[contains(text(), '%s')]" % day
        )
        return self._is_day_element_open(day_element)

    def _is_day_element_open(self, el: WebElement) -> bool:
        classes = el.get_attribute("class")
        return "disabled" not in str(classes)
