from selenium.webdriver.support.ui import Select
import unittest
import datetime
from functions import *
from selenium import webdriver

class StatusAndDisruptions(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.nationalrail.co.uk/plan-a-journey/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # 1.3.1
    def test_find_connection(self):
        privacy_popup(self)
        open_search_journey(self)
        departure_station_name = pick_departure_station(self)
        arrival_station_name = pick_arrival_station(self)
        show_times_prices(self)
        summary_departure = get_summary(self)

        self.assertIn(departure_station_name, summary_departure)
        self.assertIn(arrival_station_name, summary_departure)

    # 1.3.2
    def test_find_connection_with_avoid(self):
        privacy_popup(self)
        open_search_journey(self)
        pick_departure_station(self)
        pick_arrival_station(self)

        route_details = self.driver.find_element(By.XPATH, '/html/body/div[2]/dialog/div/div[2]/form/section/button')
        route_details.click()
        route_details_dropdown = Select(self.driver.find_element(By.ID, 'route-constraint-type'))
        route_details_dropdown.select_by_visible_text('Avoid')

        avoid_station = self.driver.find_element(By.ID, 'route-constraint-station')
        avoid_station.click()
        avoid_station_name = "London " + random.choice(london_list)
        avoid_station.send_keys(avoid_station_name)
        avoid_station_select = self.driver.find_element(By.ID, 'sp-route-constraint-station-result-0')
        avoid_station_select.click()

        show_times_prices(self)
        summary_departure = get_summary(self)

        self.assertIn(avoid_station_name, summary_departure)

    # 1.3.3
    def test_find_connection_with_not_change_at(self):
        privacy_popup(self)
        open_search_journey(self)
        pick_departure_station(self)
        pick_arrival_station(self)

        route_details = self.driver.find_element(By.XPATH,
                                                     '/html/body/div[2]/dialog/div/div[2]/form/section/button')
        route_details.click()
        route_details_dropdown = Select(self.driver.find_element(By.ID, 'route-constraint-type'))
        route_details_dropdown.select_by_visible_text('Do Not Change At')

        not_change_at_station = self.driver.find_element(By.ID, 'route-constraint-station')
        not_change_at_station.click()
        not_change_at_name = "London " + random.choice(london_list)
        not_change_at_station.send_keys(not_change_at_name)
        not_change_at_station_select = self.driver.find_element(By.ID, 'sp-route-constraint-station-result-0')
        not_change_at_station_select.click()

        show_times_prices(self)
        summary_departure = get_summary(self)

        self.assertIn(not_change_at_name, summary_departure)

    # 1.3.4
    def test_find_connection_tomorrow(self):
        privacy_popup(self)
        open_search_journey(self)
        pick_departure_station(self)
        pick_arrival_station(self)

        open_calendar = self.driver.find_element(By.ID, 'leaving-date')
        open_calendar.click()
        tomorrow_button = self.driver.find_element(By.ID, 'button-tomorrow-leaving')
        tomorrow_button.click()
        show_times_prices(self)

        journey_summary = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[1]/div[1]/div/div/div/div[2]/div[1]/span[1]').text
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        change_date_format = tomorrow.strftime("%d %b %Y")

        self.assertIn(change_date_format, journey_summary)

    def tearDown(self):
        self.driver.quit()
