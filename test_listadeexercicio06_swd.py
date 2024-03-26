# 1 - Bibliotecas
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Classe 
class Teste_Produtos():

    # 2.1 Atributos
    url = "https://www.saucedemo.com"              # endereço do site 

    # 2.2 Funções e Métodos
    def setup_method(self, method):               
        self.driver = webdriver.Chrome()          
        self.driver.implicitly_wait(10)            

    def teardown_method(self, method):             
        self.driver.quit()                         # encerra / destrói o objeto do Selenium WebDriver da memória

    def test_selecionar_produto(self):             # método de teste
        self.driver.get(self.url)                  # abre o navegador
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")     
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")     
        self.driver.find_element(By.ID, "login-button").click () 

        
        assert self.driver.find_element(By.CSS_SELECTOR, "span.title").text =="Products"  #confirma se está escrito Products no elemento
        assert self.driver.find_element(By.ID, "item_4_title_link"). text == "Sauce Labs Backpack" #confirma se está escrito Sauce Labs Backpack no elemento
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price").text == (
            "$29.99")
        
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click () #clique no botão Add to cart
        assert self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge"). text == "1"
        self.driver.find_element(By.CSS_SELECTOR,".shopping_cart_badge").click ()
        
        assert self.driver.find_element(By.CSS_SELECTOR, ".title"). text == "Your Cart"
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item_name"). text =="Sauce Labs Backpack"
        assert self.driver.find_element(By.CSS_SELECTOR, ".cart_quantity").text == "1"
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item_price").text =="$29.99"

        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click() # clique para remover o produto do carrinho
        self.driver.find_element(By.ID,"react-burger-menu-btn").click() #clique no menu lateral
        self.driver.find_element(By.ID, "logout_sidebar_link").click() # faz logoff no site






    

        
