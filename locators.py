from selenium.webdriver.common.by import By

class  HomeLocators(object):
    TxtBox_search= (By.NAME, 'q')
    Btn_GoogleSearch= (By.XPATH, "//div [@class= 'FPdoLc tfB0Bf']"
                                 "//input [@name= 'btnK' and @value= 'Google Search']")
    Btn_clear= (By.XPATH, "//span [@class= 'lBbtTb z1asCe rzyADb']")

class SearchPageLocators(object):
     TxtBox_search= (By.XPATH, "//input [@class='gLFyf gsfi']")
     Txt_results= (By.XPATH, "//div [@id='result-stats']")

