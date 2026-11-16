import os
from pymongo import MongoClient

# Pega a string de conexão configurada nas Variáveis de Ambiente da Azure
MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client['livraria_db']
collection = db['livros']  # <-- Aqui fechou o parêntese certinho
