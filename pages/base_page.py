from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def go_to_choice(self, how, what):  # выбираем что-то и кликаем
        choice = self.browser.find_element(how, what)
        choice.click()

    def get_text(self, how, what):
        return self.browser.find_element(how, what).text

    def waiting_element(self, how, what):
        WebDriverWait(self.browser, 20).until(EC.visibility_of_all_elements_located((how, what)))
