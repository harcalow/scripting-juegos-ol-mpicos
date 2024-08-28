from storage import create_table
from scraper import open_page,close_page
from parser import logic_medal_table
def main():
    print("Ejecutando primera parte")
    create_table()
    driver=open_page()
    logic_medal_table(driver)
    close_page(driver)
    
if __name__ == "__main__":
    main()