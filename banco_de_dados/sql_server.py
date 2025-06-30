# SQL Server é um sistema de gerenciamento de banco de dados relacional desenvolvido pela Microsoft. Ele é amplamente utilizado para armazenar e gerenciar grandes volumes de dados, oferecendo recursos avançados de segurança, escalabilidade e desempenho. SQL Server suporta a linguagem SQL (Structured Query Language) para consultas e manipulação de dados, além de fornecer ferramentas para administração, monitoramento e otimização do banco de dados.
import pyodbc
class SQLServerDB:
    def __init__(self, server: str, database: str, username: str, password: str):
        """Inicializa a conexão com o banco de dados SQL Server."""
        self.connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        self.connection = pyodbc.connect(self.connection_string)
        self.cursor = self.connection.cursor()

    def execute_query(self, query: str):
        """Executa uma consulta SQL."""
        self.cursor.execute(query)
        self.connection.commit()

    def fetch_all(self, query: str):
        """Executa uma consulta SQL e retorna todos os resultados."""
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        """Fecha a conexão com o banco de dados."""
        self.cursor.close()
        self.connection.close()
        
# Exemplo de uso
# db = SQLServerDB(server='localhost', database='testdb', username='user', password='password')
# db.execute_query("CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY, name NVARCHAR(100))")
# db.execute_query("INSERT INTO users (id, name) VALUES (1, 'John Doe')")
# results = db.fetch_all("SELECT * FROM users")
# for row in results:
#     print(row)
# db.close()
# Este exemplo demonstra como criar uma tabela, inserir dados e consultar registros em um banco de dados SQL Server usando a biblioteca `pyodbc`. É importante garantir que o driver ODBC correto esteja instalado e configurado no sistema para que a conexão funcione corretamente. Além disso, é recomendável tratar exceções e erros de conexão para garantir a robustez do código em aplicações reais.
# Certifique-se de que o driver ODBC para SQL Server esteja instalado no seu sistema.