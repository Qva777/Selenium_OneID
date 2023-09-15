from selenium_config import driver, preparing_to_task
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Сonstants import Selectors, UserData


def task_three():
    """ Increase capital """

    preparing_to_task()
    print("Starting task two")

    element = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located((By.XPATH, Selectors.FIND_USER_BY_PINFL_INCREASE)))
    element.click()
    print(r'Click \'reduction capital\' button ')

    element = WebDriverWait(driver, 240).until(EC.presence_of_element_located((By.XPATH, Selectors.UPLOAD_PDF)))
    file_path = UserData.PDF_FILE_PATH
    element.send_keys(file_path)
    print('PDF has been Upload')

    element = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.INCREASE_CAPITAL)))
    element.clear()
    element.send_keys(UserData.INCREASE_CAPITAL_SUM)
    print('Input capital number')

    element = WebDriverWait(driver, 240).until(EC.presence_of_element_located((By.XPATH, Selectors.SAVE_BUTTON)))
    element.click()
    print('Press saved')

    """ END THREE TASK """
