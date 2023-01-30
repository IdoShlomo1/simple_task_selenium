from .browser import Browser

DEFAULT_TIMEOUT = 30


class Page:
    URL = "https://connecteam.com/"

    def __init__(self, browser: Browser):
        self.browser = browser

    def __getattr__(self, item):
        try:
            return getattr(super(), item)
        except AttributeError:
            return getattr(self.browser, item)

    def is_in_page(self):
        ...

    def open(self, path=''):
        self.browser.get(self.URL + path)


class Component:
    def __init__(self, browser: Browser):
        self.browser = browser
