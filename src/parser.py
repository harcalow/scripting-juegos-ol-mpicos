from selenium import webdriver
import time
from scraper import element_exists,close_page,data,data_sports,test_data,click_button
def logic_medal_table(driver):
    index=0
    xpath=f"//div[@data-index='{index}']"
    while(element_exists(driver,xpath)):
        key=data(driver,xpath)
        if key != "":
            medal_table_by_sport(driver,index,key)
        index+=1
        xpath=f"//div[@data-index='{index}']"

def medal_table_by_sport(driver,index,key):
    index_by_sport=1
    click_button(driver,f"//div[@data-index='{index}']//button")
    xpath=f"//div[@data-index='{index}']//div[@class='emotion-srm-1oyaqcr elzx0n30'][{index_by_sport}]"
    while(element_exists(driver,xpath)):
        key_two=data_sports(driver,xpath,key)
        medal_table_by_sportsman(driver,index,index_by_sport,key,key_two)
        index_by_sport+=1
        xpath=f"//div[@data-index='{index}']//div[@class='emotion-srm-1oyaqcr elzx0n30'][{index_by_sport}]"

def medal_table_by_sportsman(driver,index,index_sport,key,key_two):
    index_by_sportsman=1
    click_button(driver,f"//div[@data-index='{index}']//div[@class='emotion-srm-1oyaqcr elzx0n30'][{index_sport}]//button")
    xpath=f"//div[@data-index='{index}']//div[@class='emotion-srm-6l9pan'][{index_sport}]//div[@class='emotion-srm-14s0sqk e1nfau490'][{index_by_sportsman}]"
    while(element_exists(driver,xpath)):
        test_data(driver,xpath,key,key_two)
        index_by_sportsman+=1
        xpath=f"//div[@data-index='{index}']//div[@class='emotion-srm-6l9pan'][{index_sport}]//div[@class='emotion-srm-14s0sqk e1nfau490'][{index_by_sportsman}]"
