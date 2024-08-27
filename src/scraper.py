from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from storage import create_table, insert_value,insert_value_data_sports
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
        action = ActionChains(driver)
        action.move_to_element(container).perform()
        values = container.text.split('\n')
        print(values)
        if container.text.strip() != "":
            insert_value(int(values[0]),values[1],int(values[2]),int(values[3]),int(values[4]),int(values[5]))
        return values[1]
            
def data_sports(driver,xpath,key):
    if element_exists (driver,xpath):   
        container = driver.find_element(by=By.XPATH, value=xpath)
        action = ActionChains(driver)
        action.move_to_element(container).perform()
        values = container.text.split('\n')
        print(values)
        if container.text.strip() != "":
            insert_value_data_sports(key,(values[0]),int(values[1]),int(values[2]),int(values[3]),int(values[4]))

def test_data(driver,xpath):
    if element_exists (driver,xpath):   
        container = driver.find_element(by=By.XPATH, value=xpath)
        action = ActionChains(driver)
        action.move_to_element(container).perform()
        values = container.text.split('\n')
        print(values)
        try:
            # Espera hasta que el elemento <a> esté presente
            link = WebDriverWait(container, 5).until(
                EC.presence_of_element_located((By.TAG_NAME, "a"))
            )
            href_value = link.get_attribute("href")
            print("Enlace HREF:", href_value)
        except (NoSuchElementException, TimeoutException):
            print("No se encontró el enlace <a> en el contenedor.")



def element_exists(driver, xpath):
    try:
        # Intenta encontrar el elemento con el XPath dado
        driver.find_element(by=By.XPATH, value=xpath)
        return True
    except NoSuchElementException:
        # Si se lanza la excepción, el elemento no existe
        return False
    
def click_button(driver,xpath):
    wait = WebDriverWait(driver, 100)
    boton = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    boton.click() 