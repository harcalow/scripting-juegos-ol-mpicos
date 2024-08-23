from selenium import webdriver
from storage import create_table
from scraper import open_page,close_page
from parser import logic
def main():
    create_table()
    driver=open_page()
    logic(driver)
    close_page(driver)
   
if __name__ == "__main__":
    main()