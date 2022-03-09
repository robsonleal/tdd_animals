from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AnimalsTestCase(LiveServerTestCase):
    def setUp(self):
        """ Executado no inicio de cada teste para subir um servidor de testes """
        self.browser = webdriver.Chrome('/home/robson/Projects/tdd-animals/chromedriver')

    def tearDown(self):
        """ Executado no final de cada teste para destruir o servidor de testes """
        self.browser.quit()

    def test_user_acess(self):
        """ Teste se o usuário consegue acessar o site e fazer uma busca """
        # História do usuário:
        # Vini quer conhecer mais sobre os animais ...
        # Ele encontra o Busca Animal e decidi conhecer o site
        self.browser.get(self.live_server_url + '/')
        time.sleep(1)

        # Logo quando entra na página percebe o título principal Busca Animal
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Animal', brand_element.text)
        
        # Ele vê um campo para pesquisar animais pelo nome. 
        
        # Ele pesquisa por Leão e clica no botão pesquisar.

        # O site exibe 4 caracteristicas do animal pesquisado.

        # Ele desiste de adotar um leão.
