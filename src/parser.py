from selenium import webdriver
from scraper import element_exists,close_page,data
def logic(driver):
    index=0
    xpath=f"//div[@data-index='{index}']"
    while(element_exists(driver,xpath)):
        data(driver,xpath)
        index+=1
        xpath=f"//div[@data-index='{index}']"