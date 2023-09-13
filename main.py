import time
import pickle

from selenium import webdriver
from selenium_config import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Сonstants import Selectors, UserData

# Main url
url_to_open = 'https://id.egov.uz/'

# chrome_options = Options()
# chrome_options.add_argument('--start-maximized')
# user_agent = (
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
#     "(KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36")
# chrome_options.add_argument(f'user-agent={user_agent}')
#
# driver = webdriver.Chrome(options=chrome_options)

driver.get(url_to_open)

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.MOBILE_ID)))
    element.click()
    print('pressed')

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.INPUT_PHONE_NUMBER)))
    element.send_keys(UserData.PHONE_NUMBER)
    print('Phone number has been input')

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.SEND_SMS)))
    element.click()
    print('SMS has been sent')

    time.sleep(240)
    print("woke up")

    pickle.dump(driver.get_cookies(), open(f"{UserData.PHONE_NUMBER}_cookies", "wb"))
    print("signed up")

    driver.get('https://office.birdarcha.uz/')
    print('Redirected to the office')

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.LOGIN_BIRDARCHA)))
    element.click()
    print('login birdarcha')
    driver.get('https://office.birdarcha.uz/application/legal-entity')
    print('Redirected to the legal entity page')

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.ADD_FILTER)))
    element.click()
    print('Filter menu has been open')

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Selectors.SELECT_INN)))
    element.click()
    print('select INN')

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.PRESS_ON_INN)))
    element.click()
    print('Press on INN')

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.INPUT_INN)))
    element.send_keys(UserData.INN)
    element.send_keys(Keys.RETURN)
    print('INN number has been input')

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.THREE_POINTS)))
    element.click()
    print('Press on three points')

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Selectors.CONTINUE)))
    element.click()
    print('Continue')

    time.sleep(60)

    # auth with  cookies
    # pickle.dump(driver.get_cookies(), open(f"{UserData.PHONE_NUMBER}_cookies", "wb"))

    # driver.get("https://id.egov.uz/")
    #
    # for cookie in pickle.load(open(f"{UserData.PHONE_NUMBER}_cookies", "rb")):
    #     driver.add_cookie(cookie)
    #
    # # time.sleep(10)
    # driver.refresh()

except Exception as e:
    print(f"An error occurred: {str(e)}")

time.sleep(2000000)
driver.quit()
