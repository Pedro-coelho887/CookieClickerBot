import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as clicker
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException,StaleElementReferenceException
import keyboard

#inicializando o web driver e buscando o site do Cooki Clicker
cService = webdriver.ChromeService(executable_path="C:\\Users\\pedro\\OneDrive\\Documentos\\Chromedriver\\chromedriver-win64\\chromedriver.exe")
cookiepage = webdriver.Chrome(service = cService)
cookiepage.get('https://orteil.dashnet.org/cookieclicker/')
time.sleep(5)

#mudando o indioma
language=cookiepage.find_element(By.ID,"langSelect-PT-BR")
time.sleep(1)
language.click()
time.sleep(4)
#mudando o nome da padaria
changename=cookiepage.find_element(By.ID,"bakeryName")
time.sleep(1)
changename.click()
time.sleep(2)
clicker.write('Paraspadaria')
time.sleep(1)
clicker.press('enter')
time.sleep(2)
#Iniciando jogo
print('Segure ctrl+space para parar:')
limit=50
while True:
    #condição para interromper cliques
    if keyboard.is_pressed('ctrl+space'):
        print('Pressionou!')
        break
    #Categorizando construções
    products=[]
    for i in range(8,-1,-1):
        product_id="product{}".format(i)
        try:
            product_element=cookiepage.find_element(By.ID,product_id)
            products.append(product_element)
        except NoSuchElementException:
            pass
    count=0
    #Clickando determinado número de vezes no cookie
    while count<limit:
        bigcookie=cookiepage.find_element(By.ID,"bigCookie")
        bigcookie.click()
        count+=1
    limit+=20
    #Clickando no upgrade e depois nas construções disponíveis
    try:
        upgrade = cookiepage.find_element(By.ID, "upgrade0")
        upgrade.click()
    except NoSuchElementException:
        pass
    except ElementClickInterceptedException:
        pass
    except ElementNotInteractableException:
        pass
    except StaleElementReferenceException:
        pass

    for product_element in products:
        try:
            product_element.click()
        except NoSuchElementException:
            pass
        except ElementClickInterceptedException:
            pass
        except ElementNotInteractableException:
            pass
#Encerrando o navegador
finish=input('Digite qualquer tecla para encerrar tentativa:')
cookiepage.quit()
















