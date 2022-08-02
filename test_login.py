from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium_wrapper import SeleniumWrapper
from config import Config
from loginpage import LoginPage
from homepage import HomePage

def test_login(setup):
    hp = HomePage(setup)
    hp.click_login()
    lp = LoginPage(setup)
    lp.enter_email("hello.world@company.com")
    lp.enter_password("Password123")
    lp.click_login()