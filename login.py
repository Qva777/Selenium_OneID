import time
import pickle
from selenium_config import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Сonstants import Selectors, UserData


def login_start():
    """ Login session """

    # auth with  cookies
    # driver.get("https://id.egov.uz/")
    #
    # for cookie in pickle.load(open(f"{UserData.PHONE_NUMBER}_cookies", "rb")):
    #     driver.add_cookie(cookie)
    #
    # # time.sleep(10)
    # driver.refresh()

    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.LOGIN_BIRDARCHA)))
    element.click()
    print('office.birdarcha.uz')

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.MOBILE_ID)))
    element.click()
    print('Select login with number')

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.LOGIN_INPUT_PHONE_NUMBER)))
    element.clear()
    element.send_keys(UserData.PHONE_NUMBER)
    print('Phone number has been input')

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.SEND_SMS)))
    element.click()
    print('SMS has been sent')

    time.sleep(180)
    print("Woke up")

    pickle.dump(driver.get_cookies(), open(f"{UserData.PHONE_NUMBER}_cookies", "wb"))
    print("GOT Cookies, signed up")

    """ END LOGIN """
