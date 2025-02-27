# utils/request_bodies.py

# Corpo da requisição para o endpoint de login
LOGIN_BODY = {
    "username": "",  # Será preenchido dinamicamente
    "password": ""   # Será preenchido dinamicamente
}

FIND_ALL_PRODUCTS_CUSTOM_BODY = {
    "webstore_id": "0ZEKj000000ox4zOAA",
    "account_id": "001Db000017ietDIAQ",
    "fields": ["Name", "ExternalId__c"],
    "search_fields": ["Family", "Keywords__c", "Name", "ProductCode", "StockKeepingUnit", "StockKeepingUnitSKU__c"],
    "page": 0,
    "page_size": 20,
    "category_id": "0ZGDb0000004uqxOAA",
    "sort_rule_id": "",
    "fifo_filters": ["Verde", "Vermelho"]
}

FIND_CREDIT_LIMIT_BODY = {  
    "account_id": "001Db000017ietDIAQ"
}

FIND_DELIVERY_WINDOW_BODY = {
    "account_id": "001Db000017bpCgIAI",
    "has_fifo": False
}

FIND_PAYMENTS_CONDITIONS_BODY = {
    "account_id": "001Db000017ietDIAQ"
}

FIND_PRODUCTS_FIFO = {
    "account_id": "001Db000017ietDIAQ",
    "webstore_id": "0ZEKj000000ox4zOAA",
    "skus": [],
    "categories": [],
    "brands": [],
    "types": []
}