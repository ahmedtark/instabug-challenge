from locators import HomeLocators

class Homepage():
    def __init__(self, driver):
        """Initializes attributes with their Xpath"""

        self.driver= driver
        self.search= HomeLocators.TxtBox_search
        self.go= HomeLocators.Btn_GoogleSearch
        self.clear= HomeLocators.Btn_clear

    def check_title(self):
        """ checks the correct page is loaded
            return: correct page (True), wrong page (False)
        """
        return True if self.driver.title == "Google" else False

    def search_empty(self):
        """ checks if the search box is empty
            return: clear (True), filled (False)
        """
        return True if not self.driver.find_element_by_xpath(self.search).getAttribute("value") else False

    def search_text(self, text, clear= 0):
        """ inputs the required search term to the searchbox,
            parameters: - text: takes the required searchterm
                        - clear: if equals "1" then the clear button is pressed to empty searchbox
            no return
        """
        self.driver.find_element_by_xpath(self.search).send_keys(text)
        if clear== 1:
            self.driver.find_element_by_xpath(self.clear).click()

    def search_button(self):
        """ Clicks the "Google Search" button
            no return
        """
        self.driver.find_element_by_xpath(self.go).click()


