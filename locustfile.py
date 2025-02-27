from locust import HttpUser, task, between
import json
import os
import logging
from dotenv import load_dotenv
from utils.request_bodies import * # Importa todos os corpos das requisições

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("locust")

class ApiUser(HttpUser):
    wait_time = between(1, 2.5)
    host = os.getenv("BASE_URL")  # Usa o host do .env
    token = None

    def login(self):
        """
        Realiza o login e retorna o token.
        """
        headers = {
            'Content-Type': 'application/json'
        }
        # Preenche o corpo da requisição de login com as credenciais do .env
        login_body = LOGIN_BODY.copy()
        login_body["username"] = os.getenv("USERNAME_CENTRAL")
        login_body["password"] = os.getenv("PASSWORD_CENTRAL")

        response = self.client.post("/services/apexrest/ecommerce/login", name="tokenLogin", headers=headers,
                                    data=json.dumps(login_body))
        
        # Imprime o token no log, independentemente do status da resposta
        if response.status_code == 200:
            self.token = response.json().get("token")
            logger.info(f"Token gerado: {self.token}")
        else:
            self.token = None
            logger.error(f"Falha ao gerar o token. Status code: {response.status_code}. Resposta: {response.text}")

    @task
    def findAllProductsCustom(self):
        """
        Executa o login antes de cada requisição e utiliza o token gerado.
        """
        # Executa o login para garantir que o token seja atualizado
        self.login()

        if not self.token:
            logger.error("Token não disponível. A requisição não será enviada.")
            return

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }
        # Usa o corpo da requisição armazenado em request_bodies.py
        response = self.client.post("/services/apexrest/ecommerce/product/ordered", name="findAllProductsCustom", headers=headers,
                                    data=json.dumps(FIND_ALL_PRODUCTS_CUSTOM_BODY))
        
        if response.status_code == 200:
            logger.info(f"Requisição findAllProductsCustom realizada com sucesso. Token utilizado: {self.token}")
        else:
            logger.error(f"Falha na requisição findAllProductsCustom. Status code: {response.status_code}. Token utilizado: {self.token}")
            
    @task
    def findCreditLimit(self):
        """
        Executa o login antes de cada requisição e utiliza o token gerado.
        """
        # Executa o login para garantir que o token seja atualizado
        self.login()

        if not self.token:
            logger.error("Token não disponível. A requisição não será enviada.")
            return

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }
        # Usa o corpo da requisição armazenado em request_bodies.py
        response = self.client.post("/services/apexrest/ecommerce/credit", name="findCreditLimit", headers=headers,
                                    data=json.dumps(FIND_CREDIT_LIMIT_BODY))
        
        if response.status_code == 200:
            logger.info(f"Requisição findCreditLimit realizada com sucesso.")
        else:
            logger.error(f"Falha na requisição findCreditLimit. Status code: {response.status_code}")
            
    @task
    def findDeliveryWindow(self):
        """
        Executa o login antes de cada requisição e utiliza o token gerado.
        """
        # Executa o login para garantir que o token seja atualizado
        self.login()

        if not self.token:
            logger.error("Token não disponível. A requisição não será enviada.")
            return

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }
        # Usa o corpo da requisição armazenado em request_bodies.py
        response = self.client.post("/services/apexrest/ecommerce/credit", name="findDeliveryWindow", 
                                    headers=headers, data=json.dumps(FIND_DELIVERY_WINDOW_BODY))
        
        if response.status_code == 200:
            logger.info(f"Requisição findDeliveryWindow realizada com sucesso.")
        else:
            logger.error(f"Falha na requisição findDeliveryWindow. Status code: {response.status_code}")
    
    @task
    def findPaymentConditions(self):
        """
        Executa o login antes de cada requisição e utiliza o token gerado.
        """
        # Executa o login para garantir que o token seja atualizado
        self.login()

        if not self.token:
            logger.error("Token não disponível. A requisição não será enviada.")
            return

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }
        # Usa o corpo da requisição armazenado em request_bodies.py
        response = self.client.post("/services/apexrest/ecommerce/credit", name="findPaymentConditions", 
                                    headers=headers, data=json.dumps(FIND_PAYMENTS_CONDITIONS_BODY))
        
        if response.status_code == 200:
            logger.info(f"Requisição findPaymentConditions realizada com sucesso.")
        else:
            logger.error(f"Falha na requisição findPaymentConditions. Status code: {response.status_code}")
            
    @task
    def findFifoProducts(self):
        """
        Executa o login antes de cada requisição e utiliza o token gerado.
        """
        # Executa o login para garantir que o token seja atualizado
        self.login()

        if not self.token:
            logger.error("Token não disponível. A requisição não será enviada.")
            return

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }
        # Usa o corpo da requisição armazenado em request_bodies.py
        response = self.client.post("/services/apexrest/ecommerce/product/fifo", name="findFifoProducts", 
                                    headers=headers, data=json.dumps(FIND_PRODUCTS_FIFO))
        
        if response.status_code == 200:
            logger.info(f"Requisição findFifoProducts realizada com sucesso.")
        else:
            logger.error(f"Falha na requisição findFifoProducts. Status code: {response.status_code}")
            
    @task
    def getAccountsContacts(self):
        """
        Executa o login antes de cada requisição e utiliza o token gerado.
        """
        # Executa o login para garantir que o token seja atualizado
        self.login()

        if not self.token:
            logger.error("Token não disponível. A requisição não será enviada.")
            return

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }
        # Usa o corpo da requisição armazenado em request_bodies.py
        response = self.client.get("/services/apexrest/ecommerce/account/001Db000017ietDIAQ", name="getAccountsContacts", 
                                    headers=headers)
        
        if response.status_code == 200:
            logger.info(f"Requisição getAccountsContacts realizada com sucesso.")
        else:
            logger.error(f"Falha na requisição getAccountsContacts. Status code: {response.status_code}")
            
    @task
    def getDeliveryAdress(self):
        """
        Executa o login antes de cada requisição e utiliza o token gerado.
        """
        # Executa o login para garantir que o token seja atualizado
        self.login()

        if not self.token:
            logger.error("Token não disponível. A requisição não será enviada.")
            return

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }
        # Usa o corpo da requisição armazenado em request_bodies.py
        response = self.client.get("/services/data/v62.0/commerce/webstores/0ZEKj000000ox4zOAA/accounts/001Db000017ietGIAQ/addresses", name="getDeliveryAdress", 
                                    headers=headers)
        
        if response.status_code == 200:
            logger.info(f"Requisição getDeliveryAdress realizada com sucesso.")
        else:
            logger.error(f"Falha na requisição getDeliveryAdress. Status code: {response.status_code}")