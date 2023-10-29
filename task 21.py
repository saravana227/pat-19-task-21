from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class ZenPortalAutomation:
    def __init__(self, base_url):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.base_url = 'https://www.saucedemo.com/'

    def login(self, username, password):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        # Display cookies before login
        print("Cookies before login:")
        self.display_cookies()

        username_field = self.driver.find_element(by=By.ID, value="user-name")
        password_field = self.driver.find_element(by=By.ID, value="password")
        login_button = self.driver.find_element(by=By.ID, value="login-button")

        username_field.send_keys('standard_user')
        password_field.send_keys('secret_sauce')
        login_button.click()

        # Display cookies after login
        print("\nCookies after login:")
        self.display_cookies()

    def logout(self):
        menu_button = self.driver.find_element(by=By.ID, value="react-burger-menu-btn")
        logout_button = self.driver.find_element(by=By.ID, value="logout_sidebar_link")

        menu_button.click()
        logout_button.click()

        # Display cookies after logout
        print("\nCookies after logout:")
        self.display_cookies()

    def display_cookies(self):
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            print(f"{cookie['name']}: {cookie['value']}")

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    base_url = "https://www.saucedemo.com"
    username = "your_username"
    password = "your_password"

    automation = ZenPortalAutomation(base_url)
    automation.login(username, password)
    automation.logout()
    automation.close()