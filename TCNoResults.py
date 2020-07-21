import Homepage
import SearchPage
import SetUp
import unittest

class NoResults(SetUp):
    def test_no_results(self):
        home= Homepage.Homepage()
        searchPage= SearchPage.SearchPage()
        assert home.check_title(), "This is not Google.com"
        home.search_text(text="wd23edswssdcaew32")
        home.search_button()
        assert searchPage.check_title("wd23edswssdcaew32"), "wrong search page loaded"
        searchPage.verify_search("wd23edswssdcaew32")
        assert "did not match any documents" in searchPage.get_results()



if __name__ == "__main__":
    unittest.main()
