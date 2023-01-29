import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True)
def web_driver(request):
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.close()
    chrome_driver.quit()

