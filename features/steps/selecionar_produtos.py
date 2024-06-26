# 1 - Bibliotecas/ Imports
import time
from behave import given, when, then 
from selenium import webdriver 
from selenium.webdriver.common.by import By


@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    #setup /inicialização
    context.driver = webdriver.Chrome()     # instanciar o objeto do Selenium Webdriver especializado para o Chrome
    context.driver.maximize_window ()       # maximizar a janela do navegador
    context.driver.implicitly_wait (10)     #esperar até 10 segundos por qualquer elemento
    #Passo em si
    context.driver.get("https://www.saucedemo.com")    # abrir o navegador no endereço do site alvo

@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys (usuario)
    context.driver.find_element(By.ID, "password").send_keys (senha)
    context.driver.find_element(By.ID, "login-button").click()
    

@then(u'sou direcionado para página Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR,".title").text == "Products"
    time.sleep(2) # espera por 2 segundos - remover depois - alfinete

    #teardown / encerramento
    context.driver.quit ()
    
    @then(u'exibe a mensagem de erro no login')
    def step_impl(context):
        #validar a mensagem de erro
        assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == "Epic sadface: Username and password do not match any user in this service"

    context.driver.quit ()
    
  