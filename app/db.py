import os
from pymongo import MongoClient

# Pega a string de conexão configurada nas Variáveis de Ambiente da Azure
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["livraria_db"]
collection = db["livros"]

# Cadastra os 10 livros se a coleção estiver vazia
if collection.count_documents({}) == 0:
  livros_iniciais = [
      {"titulo": "Engenharia de Software", "autor": "Ian Sommerville"},
      {"titulo": "Clean Code", "autor": "Robert C. Martin"},
      {"titulo": "Arquitetura Limpa", "autor": "Robert C. Martin"},
      {"titulo": "Entendendo Algoritmos", "autor": "Aditya Y. Bhargava"},
      {"titulo": "O Programador Pragmático", "autor": "Andrew Hunt"},
      {"titulo": "Padrões de Projetos", "autor": "Erich Gamma"},
      {"titulo": "Refatoração", "autor": "Martin Fowler"},
      {
          "titulo": "Estruturas de Dados e Algoritmos em Python",
          "autor": "Michael T. Goodrich",
      },
      {"titulo": "Python Fluente", "autor": "Luciano Ramalho"},
      {
          "titulo": "Microsserviços Prontos para a Produção",
          "autor": "Susan J. Fowler",
      },
  ]
  collection.insert_many(livros_iniciais)
  print("10 livros cadastrados no Cosmos DB com sucesso!")
