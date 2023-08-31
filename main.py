from Test_Data import data
from Test_Locators import locators

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

class Anirudh:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

    def forgot_password_link_validation(self):
        self.driver.find_element(by=By.XPATH, value=locators.Locators().forgot_password).click()
        self.driver.find_element(by=By.NAME, value=locators.Locators().reset_password_username).send_keys(data.Data().username)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().reset_password_button).click()
        msg = self.driver.find_element(by=By.XPATH, value=locators.Locators().success_message).text
        print(msg)
        self.driver.quit()

    def admin_header_validation(self):
        self.driver.find_element(by=By.NAME, value='username').send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(data.Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().login_button).click()
        self.driver.find_element(by=By.XPATH, value=locators.Locators().admin_element).click()
        print(self.driver.title)
        elements = self.driver.find_elements(by=By.CLASS_NAME, value='oxd-topbar-body-nav-tab-item')
        list1 = []
        for i in elements:
            c = i.__getattribute__('text')
            list1.append(c)
        
        print(list1)
        self.driver.quit()

    def side_pane_menu_validation(self):
        self.driver.find_element(by=By.NAME, value='username').send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(data.Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().login_button).click()
        self.driver.find_element(by=By.XPATH, value=locators.Locators().admin_element).click()
        elements1 = self.driver.find_elements(by=By.CLASS_NAME, value='oxd-main-menu-item')
        list2 = []
        for j in elements1:
            d = j.__getattribute__('text')
            list2.append(d)
        
        print(list2)
        self.driver.quit()


anirudh = Anirudh(data.Data().url)
# anirudh.forgot_password_link_validation()
# anirudh.admin_header_validation()
# anirudh.side_pane_menu_validation()