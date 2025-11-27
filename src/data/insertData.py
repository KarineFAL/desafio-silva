import psycopg2
from psycopg2 import OperationalError
import json

# Configurações de conexão
host = '172.17.0.2'
port = '5432'
database = 'catalago'
user = 'postgres'
password = 'senha'

def conectar_postgres():
    try:
        connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        return connection
    except OperationalError as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None

def carregar_dados_json(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        return json.load(file)

def inserir_dados_no_banco(dados):
    connection = conectar_postgres()
    if not connection:
        return

    cursor = connection.cursor()

    try:
        # Inserir biomas
        for tree in dados:
            for biome in tree['biomes']:  # Verifique a chave aqui
                print(tree['biomes'])                
                #cursor.execute("INSERT INTO biomes (name) VALUES (%s) ON CONFLICT (name) DO NOTHING;", (biome,))
        
        # Inserir árvores
    #     for tree in dados:
    #         cursor.execute("""
    #             INSERT INTO trees (common_name, scientific_name, description)
    #             VALUES (%s, %s, %s) RETURNING id;
    #         """, (tree['commonName'], tree['scientificName'], tree['description']))
            
    #         tree_id = cursor.fetchone()[0]
    #         print(f"Inserindo árvore: {tree['commonName']} com ID: {tree_id}")

    #         # Inserir associação árvore-bioma
    #         for biome in tree['biomes']:  # Verifique a chave aqui
    #             cursor.execute("""
    #                 INSERT INTO tree_biomes (tree_id, biome_id)
    #                 SELECT %s, id FROM biomes WHERE name = %s;
    #             """, (tree_id, biome))

    #     connection.commit()
    #     print("Dados inseridos com sucesso.")

    # except psycopg2.Error as e:
    #     print(f"Erro no PostgreSQL: {e.pgcode} - {e.pgerror}")
    #     connection.rollback()
    # except Exception as e:
    #     print(f"Erro inesperado: {str(e)}")
    #     connection.rollback()
    finally:
        cursor.close()
        connection.close()

def main():
    caminho_arquivo = '/home/karine/Documents/DesafioSilva/desafio-silva/src/data/species.json'
    dados = carregar_dados_json(caminho_arquivo)
    inserir_dados_no_banco(dados)

if __name__ == "__main__":
    main()
