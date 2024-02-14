from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


def test_log_in_passed():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("http://seleniumdemo.com")
    driver.find_element(By.XPATH, "//li[@id='menu-item-22']//a").click()
    driver.find_element(By.ID, "username").send_keys("testowanieselenium@testers.pl")
    driver.find_element(By.ID, "password").send_keys("testowanieselenium")
    # driver.find_element(By.ID, "password").send_keys(Keys.Enter)
    driver.find_element(By.NAME, "login").click()

    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()


def test_log_in_failed():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("http://seleniumdemo.com")
    driver.find_element(By.XPATH, "//li[@id='menu-item-22']//a").click()
    driver.find_element(By.ID, "username").send_keys("testowanieselenium@testers.pl")
    driver.find_element(By.ID, "password").send_keys("testowanieselenium123")
    # driver.find_element(By.ID, "password").send_keys(Keys.Enter)
    driver.find_element(By.NAME, "login").click()

    assert "ERROR: Incorrect username or password." in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error"
                                                                                     "']//li").text


