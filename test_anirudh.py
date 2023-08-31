# Pytest with POM

import pytest
from Test_Data import data
from Test_Locators import locators
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Test Suite

class Test_Anirudh:
    # Boot method to run Pytest using POM
    @pytest.fixture
    def startup(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()

    def test_forgot_password_link_validation(self, startup):
        self.url = data.Data().url
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().forgot_password).click()
        self.driver.find_element(by=By.NAME, value=locators.Locators().reset_password_username).send_keys(data.Data().username)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().reset_password_button).click()
        msg = self.driver.find_element(by=By.XPATH, value=locators.Locators().success_message).text
        assert msg == 'Reset Password link sent successfully'
        print('success message', msg)

    def test_admin_header_validation(self, startup):
        self.url = data.Data().url
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value='username').send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(data.Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().login_button).click()
        self.driver.find_element(by=By.XPATH, value=locators.Locators().admin_element).click()
        options = ['User Management', 'Job', 'Organization', 'Qualifications', 'Nationalities', 'Corporate Branding', 'More']
        elements = self.driver.find_elements(by=By.CLASS_NAME, value='oxd-topbar-body-nav-tab-item')
        list1 = []
        for i in elements:
            c = i.__getattribute__('text')
            list1.append(c)
        
        assert self.driver.title == 'OrangeHRM' and list1 == options
        print('admin page headers', list1)

    def test_side_pane_menu_validation(self, startup):
        self.url = data.Data().url
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value='username').send_keys(data.Data().username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(data.Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Locators().login_button).click()
        self.driver.find_element(by=By.XPATH, value=locators.Locators().admin_element).click()
        options1 = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard', 'Directory', 'Maintenance', 'Claim', 'Buzz']
        elements1 = self.driver.find_elements(by=By.CLASS_NAME, value='oxd-main-menu-item')
        list2 = []
        for j in elements1:
            d = j.__getattribute__('text')
            list2.append(d)
        
        assert list2 == options1
        print('side menu options', list2)
