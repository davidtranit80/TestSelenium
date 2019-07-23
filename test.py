import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class self(unittest.TestCase):
    CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = True
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)
        # self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=)
        self.driver.set_window_size(1120, 550)

    def test_autocomplete(self):
        self.driver.get("https://formy-project.herokuapp.com/autocomplete")
        autocomplete = self.driver.find_element_by_id('autocomplete')
        autocomplete.send_keys("50 Marden")
        self.driver.implicitly_wait(100)
        autocomplete_result = self.driver.find_element_by_class_name('pac-item')
        autocomplete_result.click()

    def test_radiobutton(self):
        self.driver.get("https://formy-project.herokuapp.com/radiobutton")
        radio_button1 = self.driver.find_element_by_id('radio-button-1')
        radio_button1.click()
        radio_button2 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='option2']")))
        # //radio_button2 = self.driver.find_element_by_css_selector("input[value='option2']")
        radio_button2.click()
        radio_button3 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='option3']")))
        radio_button3.click()

    def test_datepicker(self):
        self.driver.get("https://formy-project.herokuapp.com/datepicker")
        date_picker = self.driver.find_element_by_id('datepicker')
        date_picker.click()
        date_picker.send_keys("24/5/2019")
        date_picker.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()