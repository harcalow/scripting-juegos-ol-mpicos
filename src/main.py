from storage import create_table
from scraper import open_page,close_page
from parser import logic_medal_table,logic_by_sportsman
def main():
    page="https://olympics.com/es/paris-2024/medallas"
    print("Ejecutando primera parte")
    create_table()
    driver=open_page(page)
    logic_medal_table(driver)
    close_page(driver)
    
    print("Ejecutando segunda parte")
    logic_by_sportsman()
    print("Fin del proceso")
if __name__ == "__main__":
    main()