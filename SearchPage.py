import locators
class SearchPage(object):
    def __init__(self, browser):
        self.browser= browser

    def check_title(self, text):
        #checks the search page is for the correct search term
        return text in self.driver.title

    def verify_search(self, text):
        #retrieves the text in the search box and verifies it is the correct search term
        element= self.driver.find_element(locators.SearchPageLocators.TxtBox_search)
        return  text in element.getAttribute("value")

    def get_results(self):
        #retrieves the number of results found
        element= self.driver.find_element(locators.SearchPageLocators.Txt_results)
        return "did not match any documents" if "did not match any documents" in self.driver.page_source else element.getAttribute("value")
