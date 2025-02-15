from locust import HttpUser, task, between
import json
import os
import logging
from dotenv import load_dotenv
from utils.request_bodies import LOGIN_BODY, FIND_ALL_PRODUCTS_CUSTOM_BODY  # Importa os corpos das requisições

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
            'Content-Type': 'application/json',
            'Cookie': os.getenv("COOKIE")  # Usa o cookie do .env
        }
        # Preenche o corpo da requisição de login com as credenciais do .env
        login_body = LOGIN_BODY.copy()
        login_body["username"] = os.getenv("USERNAME")
        login_body["password"] = os.getenv("PASSWORD")

        response = self.client.post("/services/apexrest/ecommerce/login", headers=headers, data=json.dumps(login_body))
        
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
            'Authorization': f'Bearer {self.token}',
            'Cookie': os.getenv("COOKIE")  # Usa o cookie do .env
        }
        # Usa o corpo da requisição armazenado em request_bodies.py
        response = self.client.post("/services/apexrest/ecommerce/product/ordered", headers=headers, data=json.dumps(FIND_ALL_PRODUCTS_CUSTOM_BODY))
        
        if response.status_code == 200:
            logger.info(f"Requisição findAllProductsCustom realizada com sucesso. Token utilizado: {self.token}")
        else:
            logger.error(f"Falha na requisição findAllProductsCustom. Status code: {response.status_code}. Token utilizado: {self.token}")