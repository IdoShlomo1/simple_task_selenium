from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from .browser import Locator
from .elements import Component, Page


DEFAULT_TIMEOUT = 30


class IndexFooter(Component):
    CONTAINER = Locator(By.CSS_SELECTOR, '.section-footer')
    '.class="section-footer__menuNav accordion-opened"'
    NAV_ITEM_LINK = '//div[@id="content"]//a[contains(., "%s")]'

    def click_on_menu_nav_item(self, link_value):
        locator = Locator(By.XPATH, self.NAV_ITEM_LINK % link_value)
        self.browser.click(locator)

    def scroll_to_item_and_click(self, link_value):
        element = self.browser.find_element(Locator(By.XPATH, self.NAV_ITEM_LINK % link_value))
        self.browser.actions.move_to_element(element).click(on_element=element).perform()


class IndexPage(Page):
    URL = "https://connecteam.com/"
    COOKIE_DIALOG_BUTTON = Locator(By.CSS_SELECTOR, '#content > div.cookies-popup svg')

    def __init__(self, browser):
        super(IndexPage, self).__init__(browser)
        self.footer = IndexFooter(browser)

    def click_accept_cookies(self):
        self.wait.until(
            expected_conditions.visibility_of_element_located(
                Locator(By.CSS_SELECTOR, '#content > div.cookies-popup svg'))
        )
        self.browser.click(self.COOKIE_DIALOG_BUTTON)


class OpenCareersPage(Page):
    POSITION_LINK = 'a[href="https://connecteam.com/careers/%s/"]'
    departments = {'rnd'}

    def click_on_career_dialog_rnd(self):
        self.browser.find_element(Locator(By.CSS_SELECTOR, 'a[href="https://connecteam.com/careers/rd/"]')).click()


class CareerDepartmentPage(Page):
    POSITION_LIST = Locator(By.CSS_SELECTOR, '.careers-category__cards-list a')

    def get_position_by_index(self, position_index):
        list_of_positions = self.browser.find_elements(self.POSITION_LIST)
        list_of_positions[position_index].click()


class ApplicantForm(Component):
    FRAME = Locator(By.ID, "grnhse_iframe")
    FIRST_NAME_INPUT = Locator(By.ID, 'first_name')
    LAST_NAME_INPUT = Locator(By.ID, 'last_name')
    EMAIL_INPUT = Locator(By.ID, 'email')
    PHONE_INPUT = Locator(By.ID, 'first_name')
    LINKDIN_PROFILE_INPUT = Locator(By.ID, 'job_application_answers_attributes_0_text_value')

    def switch_to_form(self):
        self.browser.switch_to_available_frame(self.FRAME)

    def enter_first_name(self, first_name):
        self.browser.send_text(self.FIRST_NAME_INPUT, text=first_name)

    def enter_last_name(self, last_name):
        self.browser.send_text(self.LAST_NAME_INPUT, text=last_name)

    def enter_email(self, email):
        self.browser.send_text(self.EMAIL_INPUT, text=email)

    def enter_phone(self, phone):
        self.browser.send_text(self.PHONE_INPUT, text=phone)

    def enter_linkdin(self, linkdin_link):
        self.browser.send_text(self.LINKDIN_PROFILE_INPUT, text=linkdin_link)

    def fill_form(self, first_name=None, last_name=None, phone=None, link=None, email=None):
        self.switch_to_form()
        self.enter_email(email)
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_linkdin(link)
        self.enter_phone(phone)
        # click


class CareerApplicantPage(Page):
    def __init__(self, browser):
        super(CareerApplicantPage, self).__init__(browser)
        self.applicant_form = ApplicantForm(browser)


class Site:
    def __init__(self, browser):
        self.index_page = IndexPage(browser)
        self.career_department_page = CareerDepartmentPage(browser)
        self.open_career_page = OpenCareersPage(browser)
        self.career_applicant_page = CareerApplicantPage(browser)
