import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.parametrize('position_index', range(6))
def test_submit_cv(position_index, web_driver):
    wait = WebDriverWait(web_driver, 30)
    actions = ActionChains(web_driver)
    web_driver.get("https://connecteam.com/")

    cookies_consent_dialog = wait.until(expected_conditions.visibility_of_element_located(
        (By.CSS_SELECTOR, '#content > div.cookies-popup svg'))
    )
    cookies_consent_dialog.click()

    element = web_driver.find_element(*(By.XPATH, '//div[@id="content"]//a[contains(., "Careers")]'))
    actions.move_to_element(element).click(on_element=element).perform()

    web_driver.find_element(*(By.CSS_SELECTOR, 'a[href="https://connecteam.com/careers/rd/"]')).click()
    list_of_positions = web_driver.find_elements(*(By.CSS_SELECTOR, '.careers-category__cards-list a'))
    list_of_positions[position_index].click()

    wait.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.ID, "grnhse_iframe")))

    wait.until(expected_conditions.presence_of_element_located((By.ID, 'first_name'))).send_keys("First")
    wait.until(expected_conditions.presence_of_element_located((By.ID, 'last_name'))).send_keys("Last")
    wait.until(expected_conditions.presence_of_element_located((By.ID, 'email'))).send_keys("first.last@gmail.com")
    wait.until(expected_conditions.presence_of_element_located((By.ID, 'phone'))).send_keys("0547552217")
    wait.until(expected_conditions.presence_of_element_located((By.ID, 'job_application_answers_attributes_0_text_value'))).send_keys("https://my-linkdin.com")
    # wait.until(expected_conditions.element_to_be_clickable((By.ID, 'submit_app'))).click()
