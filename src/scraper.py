from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
from storage import create_table, insert_value
options = webdriver.EdgeOptions()
options.add_argument("--inprivate")
def open_page():
    try:
        driver = webdriver.Edge()
        driver.get('https://olympics.com/es/paris-2024/medallas')
        return driver
    except Exception as e:
        driver.quit()
        print("Error:", e)
def close_page(driver):
    driver.quit()

def data(driver,xpath):
    if element_exists (driver,xpath):
        container = driver.find_element(by=By.XPATH, value=xpath)
        values = container.text.split('\n')
        insert_value(values[1],int(values[2]),int(values[3]),int(values[4]),int(values[5]))

def element_exists(driver, xpath):
    try:
        # Intenta encontrar el elemento con el XPath dado
        driver.find_element(by=By.XPATH, value=xpath)
        return True
    except NoSuchElementException:
        # Si se lanza la excepción, el elemento no existe
        return False