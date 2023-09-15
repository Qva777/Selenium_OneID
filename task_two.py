from Сonstants import Selectors, UserData
from selenium_config import driver, preparing_to_task
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def task_two():
    """ Add founder """

    preparing_to_task()
    print("Starting task two")

    element = WebDriverWait(driver, 240).until(EC.presence_of_element_located((By.XPATH, Selectors.ADD_FOUNDER)))
    element.click()
    print('Pressed button "Add founder"')

    element = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located((By.XPATH, Selectors.SELECT_INDIVIDUAL)))
    element.click()
    print('Select individual person(radio button)')

    element = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located((By.XPATH, Selectors.CONTINUE_INDIVIDUAL)))
    element.click()
    print('Pressed button continue')

    element = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located((By.XPATH, Selectors.TYPE_OF_DOCUMENT)))
    element.click()
    print('Open menu type of document')

    element = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located((By.XPATH, Selectors.CITIZENS_PASSPORT)))
    element.click()
    print('Select type of document')

    element = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located((By.XPATH, Selectors.INPUT_PASSPORT_SERIES)))
    element.clear()
    element.send_keys(UserData.ID_PASPORT)
    print('Passport series')

    element = WebDriverWait(driver, 240).until(EC.presence_of_element_located((By.XPATH, Selectors.INPUT_PINFL)))
    element.clear()
    element.send_keys(UserData.PINFL)
    print('Input PINFL')

    element = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located((By.XPATH, Selectors.SEARCH_PERSON)))
    element.click()
    print('Search Person')

    element = WebDriverWait(driver, 240).until(EC.presence_of_element_located((By.XPATH, Selectors.NUMBER_CODE)))
    element.click()
    print('Click on phone code')

    element = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located((By.XPATH, Selectors.SELECT_NUMBER_CODE)))
    element.click()
    print('Click on phone code')

    element = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located((By.XPATH, Selectors.INPUT_PHONE_NUMBER_CODE)))
    element.clear()
    element.send_keys("3423844")
    print('Input phone number')

    element = WebDriverWait(driver, 240).until(EC.presence_of_element_located((By.XPATH, Selectors.INPUT_EMAIL)))
    element.clear()
    element.send_keys("invest@iman.uz")
    print('Input email')

    element = WebDriverWait(driver, 240).until(
        EC.presence_of_element_located((By.XPATH, Selectors.ADD_PERSON)))
    element.click()
    print('Pressed add person')

    """ END TASK TWO  """
