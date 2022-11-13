"""
Purpose: Automate the boring stuff...
...Someone asked me to fill out a form everyday :D
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

ggform="Goo.gle form" #Omitted real URL for security reasons
chromium_path="/snap/bin/chromium"
my_name=["Second person's name", "first person's name"]
my_location="Smart Start Can."

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_argument("--remote-debugging-port=9222")
option.binary_location = chromium_path
#option.add_argument("--headless")
#option.add_argument("disable-gpu")
caps = webdriver.DesiredCapabilities.CHROME.copy()
caps['acceptInsecureCerts'] = True

def fill_out_form(name, location):
    browser = None
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option, desired_capabilities=caps)

    browser.get(ggform)

    # Take time after opening the browser window, like a real human user :)
    sleep(10)

    ## filling the form
    namefill=browser.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    locationfill=browser.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    check0=browser.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div")
    check1=browser.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div")
    check2=browser.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div")
    check3=browser.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div")
    check4=browser.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div")
    check5=browser.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div")
    check6=browser.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div")
    check7=browser.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div")
    check8=browser.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div")
    check9=browser.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div")
    check10=browser.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div")
    check11=browser.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div")
    submitbutton=browser.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
        
    namefill.send_keys(name)
    locationfill.send_keys(my_location)
    check0.click()
    check1.click()
    check2.click()
    check3.click()
    check4.click()
    check5.click()
    check6.click()
    check7.click()
    check8.click()
    check9.click()
    check10.click()
    check11.click()

    #submitbutton.click()
    browser.quit()

    # Take time after opening the browser window, like a real human user :)
    sleep(5)

for name in my_name:
    fill_out_form(name=name, location=my_location)
