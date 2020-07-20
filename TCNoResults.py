from selenium import webdriver
import pages

class NoResults():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com/")

    def test_no_results(self):
        home= pages.Homepage()
        searchPage= pages.SearchPage()
        assert home.check_title(), "This is not Google.com"
        home.search_text(text="wd23edswssdcaew32")
        home.search_button()
        assert searchPage.check_title("wd23edswssdcaew32"), "wrong search page loaded"
        searchPage.verify_search("wd23edswssdcaew32")
        assert "did not match any documents" in searchPage.get_results()

    def close(self):
        self.driver.close()


if __name__ == "__main__":
    test= NoResults.test_no_results()
    test= NoResults.close()
