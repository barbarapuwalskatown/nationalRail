from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class MainPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    # 1.1.1
    def test_loading_main_page(self):
        self.driver.get("https://www.nationalrail.co.uk/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        railway_logo = self.driver.find_element(By.XPATH, '//*[@id="grid-row-header-0"]/div/div/div/div/div/a')
        get_railway_logo_text = railway_logo.get_attribute('aria-label')
        self.assertEqual("National Rail home", get_railway_logo_text)

    def tearDown(self):
        self.driver.quit()
