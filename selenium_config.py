import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Сonstants import Selectors, UserData

chrome_options = Options()
chrome_options.add_argument('--start-maximized')
user_agent = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
)

chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=chrome_options)


def preparing_to_task():
    """ Start before tasks """

    # driver.get('https://office.birdarcha.uz/')
    # print('Redirected to the office')
    #
    # element = WebDriverWait(driver, 60).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.LOGIN_BIRDARCHA)))
    # element.click()
    # print('office.birdarcha.uz login')
    # time.sleep(5)

    driver.get('https://office.birdarcha.uz/application/legal-entity')
    print('Redirected to the legal entity page')

    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.ADD_FILTER)))
    element.click()
    print('Filter menu has been open')

    element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, Selectors.SELECT_INN)))
    element.click()
    print('Select INN')

    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.PRESS_ON_INN)))
    element.click()
    print('Press on INN')

    time.sleep(5)
    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.INPUT_INN)))
    element.clear()
    element.send_keys(UserData.INN)
    element.send_keys(Keys.RETURN)
    print('INN number has been input')

    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.THREE_POINTS)))
    element.click()
    print('Press on three points')

    time.sleep(5)
    element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, Selectors.CONTINUE)))
    element.click()
    print('Continue')

    """ END PREPARING """
