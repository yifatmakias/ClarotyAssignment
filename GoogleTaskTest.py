from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import unittest


class GoogleTaskTest(unittest.TestCase):

    def setUp(self):
        # creates a new chrome session
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_google(self):
        driver = self.driver
        # 1. Go to google.com
        driver.get("https://www.google.com")

        # 2. Search 'Claroty'
        input_element = driver.find_element_by_name("q")
        input_element.send_keys("Claroty")
        input_element.submit()

        # 3. Print to console the results number
        print(driver.find_element_by_id("resultStats").text)

        # 4. Make sure that claroty.com is the first result's link
        results = driver.find_elements_by_css_selector('div.g')
        link = results[0].find_element_by_tag_name("a")
        href = link.get_attribute("href")
        self.assertEqual(href, 'https://www.claroty.com/')

        # 5. Go to https://www.claroty.com/careers
        driver.get("https://www.claroty.com/careers")

        # 6. Print to console the number of carriers
        careers_results = driver.find_elements_by_xpath("//*[@class='w-dyn-item']")
        print(len(careers_results))

    def tearDown(self):
        self.driver.quit()

