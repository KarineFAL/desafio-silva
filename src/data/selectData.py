import psycopg2
from psycopg2 import OperationalError

# Defina as configurações de conexão
host = '172.17.0.2'           # Ou o nome do container se estiver usando uma rede Docker personalizada
port = '5432'                 # Porta do PostgreSQL (padrão)
database = 'catalago'         # Nome do banco de dados
user = 'postgres'             # Usuário do banco de dados
password = 'senha'            # Senha do banco de dados

# Função para conectar ao banco de dados PostgreSQL
def conectar_postgres():
    try:
        # Estabelece a conexão com o banco de dados
        connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
        
        # Cria um cursor para interagir com o banco de dados
        cursor = connection.cursor()

        # Imprime a versão do PostgreSQL como uma verificação
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"Conectado ao PostgreSQL, versão: {db_version}")

        # Consulta para listar todas as tabelas no esquema 'public'
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
        tables = cursor.fetchall()
        print("Tabelas no banco de dados:")
        for table in tables:
            print(table[0])

        # Se você quiser consultar a tabela 'biomes', execute a consulta:
        try:
            cursor.execute("SELECT * FROM biomes;")
            biomes = cursor.fetchall()
            print("\nDados da tabela 'biomes':")
            for biome in biomes:
                print(biome)
        except psycopg2.errors.UndefinedTable:
            print("\nA tabela 'biomes' não existe no banco de dados.")

        # Fecha o cursor e a conexão
        cursor.close()
        connection.close()

    except OperationalError as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")

if __name__ == "__main__":
    conectar_postgres()
