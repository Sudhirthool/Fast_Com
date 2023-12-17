from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions

from selenium import webdriver

class Fast_com_page:

    Message_XPATH = (By.XPATH, "//*[@id='your-speed-message']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 40, poll_frequency=2)



    def capture_screenshot(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Message_XPATH))



