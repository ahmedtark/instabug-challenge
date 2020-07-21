import locators

class Homepage(object):

    driver.get("https://www.google.com/")

    def check_title(self):
        #checks the correct page is loaded
        return True if self.driver.title == "Google" else False

    def search_empty(self):
        #checks if the search box is empty
        return True if not self.driver.find_element(locators.HomeLocators.TxtBox_search).getAttribute("value") else False

    def search_text(self, text, empty= 0):
        #enters the required search term, if empty is equals 1 then the clear button is pressed
        element= self.driver.find_element(locators.HomeLocators.TxtBox_search)
        element.send_keys(text)
        assert element.getAttribute("value") == text, "Text is different from the search term"
        if empty== 1:
            self.driver.find_element(locators.HomeLocators.Btn_clear).click()

    def search_button(self):
        #Clicks the "Google Search" button
        self.driver.find_element(locators.HomeLocators.Btn_GoogleSearch).click()


