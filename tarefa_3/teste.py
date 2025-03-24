from pathlib import Path
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from xpath import *
from Exceptions import PageNotCaughtException

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-session-crashed-bubble")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--incognito")
    #options.add_argument('--headless')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--start-maximized") 
    options.add_argument("--window-size=2560,2000") 
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

    remote_debugging_port =  9320 #9500 
    options.add_argument(f"--remote-debugging-port={remote_debugging_port}")

    service = ChromeService()
    driver = webdriver.Chrome(service=service, options=options)

    driver.execute_cdp_cmd(
        'Network.setExtraHTTPHeaders',
        {
            "headers": {
                "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                "sec-ch-ua-platform": '"Windows"'
            }
        }
    )

    # Comando para limpar o cache
    driver.execute_cdp_cmd("Network.clearBrowserCache", {})
    driver.execute_cdp_cmd("Network.clearBrowserCookies", {})

    driver.maximize_window()

    return driver

def encontrar_elemento(driver, xpath1, xpath2):
    try:
        return driver.find_element(By.XPATH, xpath1).text
    except NoSuchElementException:
        try:
            return driver.find_element(By.XPATH, xpath2).text
        except NoSuchElementException:
            return None
        
def consult(driver, wait, url):
    driver.get(url)
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, page_validation)))
    except Exception as e:
        print(e)
        raise PageNotCaughtException("Pagina não encontrada")
    
    dados = []
    consulta = 0
    for i in range(3, 50):
        if consulta == 5:
            break
        x = 5
        nome = encontrar_elemento(driver, name1.format(i), name2.format(i))
        preco =  encontrar_elemento(driver, price1.format(i, x), price2.format(i, x))
        print(nome)
        print(preco)
        
        if nome is None or preco is None:
            continue
        linhas = preco.split("\n")
        
        produto = nome
        try:
            if len(linhas) > 1:
                preco_promocional = f"{linhas[0].replace('R$', '').replace('.', '').strip()}.{linhas[1].strip()}"
            else:
                preco_promocional = None
            
            if preco_promocional:
                preco_promocional = float(preco_promocional)

            if len(linhas) > 2:
                preco_original = linhas[2].replace("R$", "").replace(".", "").replace(",", ".").strip()
            else:
                preco_original = None 

        except IndexError as e:
            print("Erro ao acessar índice na lista 'linhas':", e)
            preco_original = None 

        parcelamento = re.search(r"em até (\d+)x de R\$(\d+,\d+)", preco.replace("\n", " "))

        if parcelamento:
            parcelas = parcelamento.group(1)
            valor_parcela = parcelamento.group(2).replace(",", ".")
        else:
            parcelas = None
            valor_parcela = None

        dados.append({
            "Produto": produto,
            "Preço Promocional": preco_promocional,
            "Preço Original": preco_original,
            "Parcelas": parcelas,
            "Valor Parcela": valor_parcela
        })
        consulta += 1

    df = pd.DataFrame(dados)
    print(df)

    df.to_csv("produtos.csv", index=False, encoding="utf-8")

    print("Arquivo CSV salvo com sucesso!")


def main():
    driver = setup_driver()
    wait = WebDriverWait(driver, 15)
    url = 'https://www.amazon.com.br/s?k=iphone&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1PFH9QLKTLVBG&sprefix=iphone%2Caps%2C286&ref=nb_sb_noss_1'
    try:
        consult(driver, wait, url )
    except PageNotCaughtException as e:
        print(f'Erro: {e}')

if __name__ == '__main__':
    main()