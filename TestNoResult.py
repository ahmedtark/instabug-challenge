import Homepage
import SearchPage
from selenium import webdriver
from datetime import datetime
import logging

driver = webdriver.Chrome()
driver.maximize_window()
now = datetime.now()
date_time = now.strftime("%d%m%y%H%M")
log_file = "LogsNoResults/" + date_time + ".log"

logging.basicConfig(filename=log_file, level=logging.DEBUG)
logging.debug('Start Test')

try:
    driver.get("https://www.google.com/?hl=en")
    home= Homepage.Homepage(driver)
    searchPage= SearchPage.SearchPage(driver)
    assert home.check_title(), "This is not Google.com"
    home.search_text(text="wd23edswssdcaew32")
    home.search_button()
    assert searchPage.check_title("wd23edswssdcaew32"), "wrong search page loaded"
    searchPage.verify_search("wd23edswssdcaew32")
    assert not searchPage.get_results()

except:
    """Recovery block when failed
    """

    driver.get_screenshot_as_file("ScreenshotsNoResults/screenshotFailure.png")
    logging.error("Test Case Failed")


else:
    """Test Case Passed
    """

    driver.get_screenshot_as_file("ScreenshotsNoResults/screenshotFinalPage.png")
    logging.info('Test Passed')

driver.close()
driver.quit()