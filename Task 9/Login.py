from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

class Data:
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"
    URL = "https://www.saucedemo.com/"
    DASHBOARD_URL = "https://www.saucedemo.com/inventory.html"

class Locators:
    username_box = "user-name"
    password_box = "password"
    submit_button = '//*[@id="login-button"]'

class SwagLabs(Data, Locators):

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.URL)
            sleep(3)
            username_box = self.driver.find_element(by=By.NAME, value=self.username_box)
            password_box = self.driver.find_element(by=By.NAME, value=self.password_box)
            submit_button = self.driver.find_element(by=By.XPATH, value=self.submit_button)
            if username_box and password_box:
                username_box.send_keys(self.USERNAME)
                password_box.send_keys(self.PASSWORD)
                if submit_button:
                    submit_button.click()
                    sleep(3)
                    return self.driver.current_url
        except Exception as error:
            print("ERROR : Something happened !", error)

    def fetch_url(self):
        if self.driver.current_url == self.DASHBOARD_URL:
            return self.driver.current_url
        else:
            return "Error: unable to fetch url"

    def fetch_title(self):
        if self.driver.current_url == self.DASHBOARD_URL:
            return self.driver.title
        else:
            return "Error: Unable to find the title"

    def extract_page_content(self):
        return self.driver.page_source

    def shutdown(self):
        self.driver.quit()
        sleep(2)
