import random
from time import sleep
from selenium.webdriver.common.by import By

london_list = ["Cannon Street", "Charing Cross", "Bridge", "Blackfriars", "Euston", "Fenchurch", "Fields",
               "Kings Cross"]
manchester_list = ["Airport", "Oxford", "Piccadilly", "Victoria"]


def privacy_popup(self=None):
    accept_privacy = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
    accept_privacy.click()


def open_search_journey(self=None):
    journey_search = self.driver.find_element(By.XPATH, '//*[@id="jp-form-preview"]/section/div/button')
    journey_search.click()


def pick_departure_station(self=None):
    departing_from = self.driver.find_element(By.XPATH, '//*[@id="jp-origin"]')
    departing_from.click()
    departure_station_name = "London " + random.choice(london_list)
    departing_from.send_keys(departure_station_name)
    departure_station = self.driver.find_element(By.ID, 'sp-jp-origin-result-0')
    departure_station.click()
    return departure_station_name


def pick_arrival_station(self=None):
    arrival = self.driver.find_element(By.XPATH, '//*[@id="jp-destination"]')
    arrival.click()
    arrival_station_name = "Manchester " + random.choice(manchester_list)
    arrival.send_keys(arrival_station_name)
    arrival_station = self.driver.find_element(By.ID, 'sp-jp-destination-result-0')
    arrival_station.click()
    return arrival_station_name


def show_times_prices(self=None):
    get_times_and_prices = self.driver.find_element(By.ID, 'button-jp')
    get_times_and_prices.click()
    sleep(10)


def get_summary(self=None):
    summary_departure = self.driver.find_element(By.ID, 'station-heading-journey-planner-query').text
    return summary_departure
