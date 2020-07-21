from locators import SearchPageLocators

class SearchPage(object):
    def __init__(self, driver):
        """Initializes attributes with their Xpath"""

        self.driver= driver
        self.search= SearchPageLocators.TxtBox_search
        self.result= SearchPageLocators.Txt_results

    def check_title(self, text):
        """ checks the loaded search page corresponds to the correct search term
            return: Correct page (True) ,Wrong page (False)
        """

        return text in self.driver.title

    def verify_search(self, text):
        """ Retrieves the text in the search box and verifies it is the correct search term
            parameters: - text: takes the intended searchterm
            return: correct term (True), wrong term (False)
        """

        return  text in self.driver.find_element_by_xpath(self.search).get_attribute("value")

    def get_results(self):
        """ Retrieves the number of results found
            return: Results found (True), No results found (False)
        """
        if "did not match any documents" in self.driver.page_source:
            return False
        else:
            return True

