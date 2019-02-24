import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager


class LoginTest(unittest.TestCase):

    def setUp(self):
        # creates a new chrome session
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_successful_login(self):
        driver = self.driver
        driver.get("https://www.phptravels.net/admin")
        driver.find_element_by_name("email").send_keys("admin@phptravels.com")
        driver.find_element_by_name("password").send_keys("demoadmin")
        driver.find_element_by_xpath("//*[@class='btn btn-primary btn-block ladda-button fadeIn animated']").click()
        driver.implicitly_wait(3)
        try:
            driver.find_element_by_xpath("//*[@class='btn btn-danger btn-sm btn-block']")
            print("Login successfully")
        except NoSuchElementException:
            print("Invalid Login Credentials")

    def test_fail_login(self):
        driver = self.driver
        driver.get("https://www.phptravels.net/admin")
        driver.find_element_by_name("email").send_keys("admin@phptravels.com")
        driver.find_element_by_name("password").send_keys("bla")
        driver.find_element_by_xpath("//*[@class='btn btn-primary btn-block ladda-button fadeIn animated']").click()
        driver.implicitly_wait(3)
        try:
            driver.find_element_by_xpath("//*[@class='btn btn-danger btn-sm btn-block']")
            print("Login successfully")
        except NoSuchElementException:
            print("Invalid Login Credentials")

    def tearDown(self):
        self.driver.quit()
