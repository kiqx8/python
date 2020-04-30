from selenium import webdriver
import time

print("""

.▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·.      ▄▄ •        • ▌ ▄ ·. ▄▄▄ .▄▄▄ .▄▄▄▄▄
▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪    ▐█ ▀ ▪       ·██ ▐███▪▀▄.▀·▀▄.▀·•██  
▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·    ▄█ ▀█▄       ▐█ ▌▐▌▐█·▐▀▀▪▄▐▀▀▪▄ ▐█.▪
▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌    ▐█▄▪▐█       ██ ██▌▐█▌▐█▄▄▌▐█▄▄▌ ▐█▌·
 ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀    ·▀▀▀▀  ▀     ▀▀  █▪▀▀▀ ▀▀▀  ▀▀▀  ▀▀▀ 

""")

chrome = webdriver.Chrome("C:/chromedriver")
chrome.get("""https://accounts.google.com/signin/v2/identifier?hl=pt-BR&passive=
true&continue=https%3A%2F%2Fwww.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin""")
           
x = input("Após ter feito login insira ok para continuar: ")

if x == "ok" or x == "OK":
    url2 = input("Link da video aula: ")
    chrome.get(url2)
    y = input("Após clicar em PARTICIPAR AGORA insira ok para continuar: ")
    if y == "ok" or y == "OK":
        chrome.find_element_by_css_selector(".KdraA > .CEJND").click()
        msg = input("Insira o texto: ")
        count = int(input("Quantas vezes enviar: "))
        
        for i in range(count):
            chrome.find_element_by_css_selector(".KHxj8b").send_keys(msg)
            time.sleep(0.1)
            chrome.find_element_by_css_selector(".hhikbc").click()
        
    
 
