from selenium.webdriver.common.by import By

    class  HomeLocators(object):
        TxtBox_search= (By.Name, 'q')
        Btn_GoogleSearch= (By.xpath, "//div [@class= 'FPdoLc tfB0Bf']"
                                     "//input [@name= 'btnK' and @value= 'Google Search']")
        Btn_clear= (By.xpath, "//span [@class= 'lBbtTb z1asCe rzyADb']")

    class SearchPageLocators(object):
        TxtBox_search= (By.xpath, "//input [@class='gLFyf gsfi']")
        Txt_results= (By.xpath, "//div [@id='result-stats']")
        
