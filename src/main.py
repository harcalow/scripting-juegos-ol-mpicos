from selenium import webdriver
from storage import create_table, insert_value
from scraper import open_page,close_page,data
from parser import logic
def main():
    create_table()
    driver=open_page()
    logic(driver)
    close_page(driver)
    # Crear una tabla llamada 'usuarios'
   
if __name__ == "__main__":
    main()