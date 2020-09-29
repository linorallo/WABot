from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
from excel_controller import getContacts
  
# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 

def loadMessage():
    message = open('message.txt' , 'r').read()
    print(message)
    return message

def showContacts():
    contacts = getContacts()
    print(contacts)
    return contacts

def send(contacts, message):
    for i in contacts:
        search_bar = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
        search_bar.send_keys(i)
        search_bar.send_keys(Keys.RETURN)
        print(i+' seleccionade')
        time.sleep(2)
        for j in range(1):
            message_box = driver.find_elements_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]')[0]
            message_box.send_keys(message)
            time.sleep(1)
            send_button = driver.find_elements_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button')[0]
            send_button.click()
            print('Mensaje a '+i+' enviado')
activate = ''
while activate != 'N' and activate != 'Y':
    activate = input('Deploy? [Y/N] ')
    if activate == 'Y':
        message = loadMessage()
        contacts = showContacts()
        send(contacts, message)
    else:
        driver.close()


