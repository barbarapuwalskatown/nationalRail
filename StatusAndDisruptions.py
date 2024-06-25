from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from _datetime import datetime
import pytz

class StatusAndDisruptions(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.nationalrail.co.uk/status-and-disruptions/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # 1.2.1
    def test_disruption_date(self):
        disruptions_date = self.driver.find_element(By.ID,"disruptions-finder-date-date").get_attribute('value')
        set_timezone = pytz.timezone("Europe/London")
        current_date = datetime.now(set_timezone)
        change_date_format = current_date.strftime("%d %b %Y")
        self.assertEqual(disruptions_date, change_date_format)
        
    def tearDown(self):
        self.driver.quit()
