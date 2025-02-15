# utils/request_bodies.py

# Corpo da requisição para o endpoint de login
LOGIN_BODY = {
    "username": "",  # Será preenchido dinamicamente
    "password": ""   # Será preenchido dinamicamente
}

# Corpo da requisição para o endpoint findAllProductsCustom
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