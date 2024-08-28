from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from storage import insert_value, insert_value_data_sports, insert_value_data_per_event, insert_sportsman

# Configurar opciones de Edge
options = webdriver.EdgeOptions()
options.add_argument("--inprivate")
def open_page(page):
    try:
        driver = webdriver.Edge(options=options)
        driver.get(page)
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
        container,values =select(driver,xpath)
        print(values)
        if container.text.strip() != "":
            insert_value(int(values[0]),values[1],int(values[2]),int(values[3]),int(values[4]),int(values[5]))
            return values[1]
        else:
            return ""
            
def data_sports(driver,xpath,key):
    if element_exists (driver,xpath):   
        container,values =select(driver,xpath)
        print(values)
        if container.text.strip() != "":
            insert_value_data_per_event(key,(values[0]),int(values[1]),int(values[2]),int(values[3]),int(values[4]))
            return values[0]
        else:
            return ""
    
def test_data(driver,xpath,key,key_two):
    if element_exists (driver,xpath):   
        container,values =select(driver,xpath)
        print(values)
        try:
            link = WebDriverWait(container, 0.1).until(
                EC.presence_of_element_located((By.TAG_NAME, "a"))
            )
            href_value = link.get_attribute("href")
            if container.text.strip() != "":
                insert_value_data_sports(key,key_two,values[0],values[1],values[2],href_value)
            print("Enlace HREF:", href_value)
        except (NoSuchElementException, TimeoutException):
            if container.text.strip() != "":
                insert_value_data_sports(key,key_two,values[0],values[1],values[2])

def select(driver, xpath):
    try:
        container = driver.find_element(by=By.XPATH, value=xpath)
        action = ActionChains(driver)
        action.move_to_element(container).perform()
        return container, container.text.split('\n')
    except NoSuchElementException as e:
        print(f"No se pudo encontrar el elemento con XPath: {xpath}. Error: {e}")
        return None, []  # Devuelve valores por defecto si no se encuentra el elemento

def data_sportsman(driver, xpath, sportsman):
    container, values = select(driver, xpath)
    if values!=[]:
        clean_values = list(map(lambda v: v.split(': ')[1].strip(), values[0:5]))
        values[0:5] = clean_values
        
        # Verificar si values[8] existe, si no, asignar un string vacío
        height = values[4] if len(values) > 4 else ''
        
        insert_sportsman(sportsman, values[0], int(values[1]), values[2], values[3], height)
    else:
        print(f"No se encontraron datos para el deportista: {sportsman}")
    
    


def element_exists(driver, xpath):
    try:
        driver.find_element(by=By.XPATH, value=xpath)
        return True
    except NoSuchElementException:
        return False
    
def click_button(driver,xpath):
    wait = WebDriverWait(driver, 10)
    boton = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    boton.click() 

