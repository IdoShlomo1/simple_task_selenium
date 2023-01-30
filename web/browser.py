from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from typing import NamedTuple


DEFAULT_TIMEOUT = 30


class Locator(NamedTuple):
    by: str
    selector: str


class Browser:
    def __init__(self, driver, download_dir):
        self.driver = driver
        self.download_dir = download_dir
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    @property
    def actions(self) -> ActionChains:
        return ActionChains(driver=self.driver)

    def click(self, locator) -> None:
        # self.wait.until(expected_conditions.visibility_of_element_located(locator))
        self.find_element(locator).click()

    def send_text(self, locator: Locator, text: str) -> None:
        self.find_element(locator).send_keys(text)

    def find_element(self, locator: Locator):
        return self.wait.until(expected_conditions.presence_of_element_located(locator))

    def find_elements(self, locator: Locator):
        return self.driver.find_elements(*locator)

    def action_click(self, locator):
        ...

    def get(self, url):
        self.driver.get(url)

    def switch_to_available_frame(self, locator):
        self.wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(locator))
