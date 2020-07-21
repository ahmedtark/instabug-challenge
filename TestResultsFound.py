import Homepage
import SearchPage
from selenium import webdriver
from datetime import datetime
import logging

driver = webdriver.Chrome()
driver.maximize_window()
now = datetime.now()
date_time = now.strftime("%d%m%y%H%M")
log_file = "LogsResultsFound/" + date_time + ".log"

logging.basicConfig(filename=log_file, level=logging.DEBUG)
logging.debug('Start Test')

try:
    driver.get("https://www.google.com/?hl=en")
    home= Homepage.Homepage(driver)
    searchPage= SearchPage.SearchPage(driver)
    assert home.check_title(), "This is not Google.com"
    home.search_text(text="bugs bunny", clear=1)
    home.search_button()
    assert home.check_title(), "This is not Google.com"
    home.search_text(text="instabug")
    home.search_button()
    assert searchPage.check_title("instabug"), "wrong search page loaded"
    searchPage.verify_search("instabug")
    logging.info(searchPage.get_results())

except:
    """Recovery block when failed
    """

    driver.get_screenshot_as_file("ScreenshotsResultsFound/screenshotFailure.png")
    logging.error("Test Case Failed")


else:
    """Test Case Passed
    """

    driver.get_screenshot_as_file("ScreenshotsResultsFound/screenshotFinalPage.png")
    logging.info('Test Passed')

driver.close()
driver.quit()
