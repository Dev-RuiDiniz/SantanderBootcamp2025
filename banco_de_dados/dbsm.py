# Banco de Dados Simples para Manipulação (dbsm)
# Banco de Dados Simples para Manipulação
# É um módulo Python que facilita a manipulação de bancos de dados SQLite, permitindo operações básicas como criação de tabelas, inserção de dados, consulta e exclusão de registros. É ideal para projetos pequenos ou para aprendizado, onde a simplicidade e a facilidade de uso são prioritárias.
import sqlite3
from typing import List, Tuple, Any
class SimpleDB:
    def __init__(self, db_name: str):
        """Inicializa a conexão com o banco de dados SQLite."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name: str, columns: List[Tuple[str, str]]):
        """Cria uma tabela no banco de dados."""
        columns_definition = ', '.join([f"{name} {dtype}" for name, dtype in columns])
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_definition})")
        self.connection.commit()

    def insert(self, table_name: str, values: Tuple[Any]):
        """Insere um registro na tabela especificada."""
        placeholders = ', '.join(['?' for _ in values])
        self.cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", values)
        self.connection.commit()

    def query(self, query: str) -> List[Tuple[Any]]:
        """Executa uma consulta SQL e retorna os resultados."""
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def delete(self, table_name: str, condition: str):
        """Exclui registros da tabela com base em uma condição."""
        self.cursor.execute(f"DELETE FROM {table_name} WHERE {condition}")
        self.connection.commit()

    def close(self):
        """Fecha a conexão com o banco de dados."""
        self.connection.close()
        