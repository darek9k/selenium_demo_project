from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import random


def test_create_account_failed():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").send_keys("testowanieselenium@testers.pl")
    driver.find_element(By.ID, "reg_password").send_keys("testowanieselenium")
    driver.find_element(By.ID, "reg_password").send_keys(Keys.ENTER)

    msg = 'An account is already registered with your email address. Please log in.'

    assert msg in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text


def test_create_account_passed():
    email = str(random.randint(0, 10000)) + "testowanieselenium@testers.pl"
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.find_element(By.ID, "reg_password").send_keys("testowanieselenium")
    driver.find_element(By.ID, "reg_password").send_keys(Keys.ENTER)
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()