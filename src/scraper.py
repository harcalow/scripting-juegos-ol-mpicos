from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
from storage import create_table, insert_value
options = webdriver.EdgeOptions()
options.add_argument("--inprivate")
def open_page():
    try:
        driver = webdriver.Edge()
        driver.get('https://olympics.com/es/paris-2024/medallas')
        terms_and_conditions(driver)
        return driver
    except Exception as e:
        driver.quit()
        print("Error:", e)
def close_page(driver):
    driver.quit()

def terms_and_conditions(driver):
    wait = WebDriverWait(driver, 100)
    boton = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="onetrust-pc-btn-handler"]')))
    boton.click()
    boton = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-cy='onetrust-reject-button']")))
    boton.click()

def data(driver,xpath):
    if element_exists (driver,xpath):
        container = driver.find_element(by=By.XPATH, value=xpath)
        driver.execute_script("arguments[0].scrollIntoView();", container)
        values = container.text.split('\n')
        if container.text.strip() != "":
            insert_value(int(values[0]),values[1],int(values[2]),int(values[3]),int(values[4]),int(values[5]))

def element_exists(driver, xpath):
    try:
        # Intenta encontrar el elemento con el XPath dado
        driver.find_element(by=By.XPATH, value=xpath)
        return True
    except NoSuchElementException:
        # Si se lanza la excepción, el elemento no existe
        return False