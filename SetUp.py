import unittest
from selenium import webdriver
class SetUp(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.chrome()
    def teardown(self):
        if (self.driver!= None):
            self.driver.close
            self.driver.quit
