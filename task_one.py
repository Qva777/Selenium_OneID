import time

from selenium_config import driver, preparing_to_task
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Сonstants import Selectors, UserData


def task_one():
    """ Reduction of capital """

    preparing_to_task()
    print("Starting task one")

    time.sleep(5)
    element = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located((By.XPATH, Selectors.FIND_USER_BY_PINFL_REDUCTION)))
    element.click()
    print(r'Click \'reduction capital\' button ')

    time.sleep(5)
    element = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.DROP_DOWN_REASON_DECREASE)))
    element.click()
    print('Open drop down menu')

    time.sleep(5)
    element = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.SELECT_MONEY_RETURN)))
    element.click()
    print('Select \'money return\'')

    time.sleep(5)
    element = WebDriverWait(driver, 240).until(EC.presence_of_element_located((By.XPATH, Selectors.CURRENT_CAPITAL)))
    capital_text = element.text
    capital_number = ''.join(filter(str.isdigit, capital_text))
    print('Current capital = ', capital_number)

    time.sleep(5)
    element = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.INPUT_REDUCTION_AMOUNT)))
    element.clear()
    element.send_keys(capital_number)
    print('Input capital number')

    time.sleep(5)
    element = WebDriverWait(driver, 240).until(EC.presence_of_element_located((By.XPATH, Selectors.UPLOAD_PDF)))
    file_path = UserData.PDF_FILE_PATH
    element.send_keys(file_path)
    print('PDF has been Upload')

    time.sleep(5)
    element = WebDriverWait(driver, 240).until(EC.presence_of_element_located((By.XPATH, Selectors.SAVE_BUTTON)))
    element.click()
    print('Press saved')

    """ END TASK ONE  """
