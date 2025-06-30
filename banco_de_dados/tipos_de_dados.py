# Dados Estruturados # são organizados em tabelas, onde cada tabela contém linhas e colunas. Cada coluna tem um tipo de dado específico, como inteiro, texto ou data. Os dados estruturados são fáceis de consultar e manipular usando SQL (Structured Query Language).

# Dados Não Estruturados # são dados que não seguem um formato predefinido, como documentos de texto, imagens, vídeos e e-mails. Eles podem ser armazenados em bancos de dados NoSQL, que permitem maior flexibilidade na estruturação dos dados. Esses dados são mais difíceis de consultar e analisar, pois não possuem uma organização rígida como os dados estruturados.

# Dados Semi-Estruturados # são uma combinação de dados estruturados e não estruturados. Eles possuem alguma organização, mas não seguem um esquema rígido. Exemplos incluem arquivos JSON, XML e YAML. Esses dados podem ser armazenados em bancos de dados NoSQL ou em sistemas de arquivos distribuídos, permitindo consultas flexíveis e análise de dados complexos.

from typing import List, Tuple, Any
class DataTypes:
    """Classe para representar diferentes tipos de dados em bancos de dados."""

    @staticmethod
    def structured_data() -> str:
        """Retorna uma descrição dos dados estruturados."""
        return ("Dados estruturados são organizados em tabelas, onde cada tabela contém linhas e colunas. "
                "Cada coluna tem um tipo de dado específico, como inteiro, texto ou data. "
                "Os dados estruturados são fáceis de consultar e manipular usando SQL (Structured Query Language).")

    @staticmethod
    def unstructured_data() -> str:
        """Retorna uma descrição dos dados não estruturados."""
        return ("Dados não estruturados são dados que não seguem um formato predefinido, como documentos de texto, "
                "imagens, vídeos e e-mails. Eles podem ser armazenados em bancos de dados NoSQL, que permitem maior "
                "flexibilidade na estruturação dos dados. Esses dados são mais difíceis de consultar e analisar, "
                "pois não possuem uma organização rígida como os dados estruturados.")

    @staticmethod
    def semi_structured_data() -> str:
        """Retorna uma descrição dos dados semi-estruturados."""
        return ("Dados semi-estruturados são uma combinação de dados estruturados e não estruturados. "
                "Eles possuem alguma organização, mas não seguem um esquema rígido. Exemplos incluem arquivos JSON, "
                "XML e YAML. Esses dados podem ser armazenados em bancos de dados NoSQL ou em sistemas de arquivos "
                "distribuídos, permitindo consultas flexíveis e análise de dados complexos.")
    @staticmethod
    def data_types() -> List[Tuple[str, str]]:
        """Retorna uma lista de tipos de dados comuns em bancos de dados."""
        return [
            ("INTEGER", "Números inteiros, sem casas decimais."),
            ("FLOAT", "Números de ponto flutuante, com casas decimais."),
            ("TEXT", "Texto ou cadeias de caracteres."),
            ("DATE", "Data no formato YYYY-MM-DD."),
            ("DATETIME", "Data e hora no formato YYYY-MM-DD HH:MM:SS."),
            ("BOOLEAN", "Valores booleanos (verdadeiro ou falso)."),
            ("BLOB", "Objetos binários grandes, como imagens ou arquivos."),
        ]
    @staticmethod
    def data_types_description() -> str:
        """Retorna uma descrição dos tipos de dados comuns em bancos de dados."""
        return ("Os tipos de dados comuns em bancos de dados incluem INTEGER, FLOAT, TEXT, DATE, DATETIME, "
                "BOOLEAN e BLOB. Cada tipo de dado tem suas próprias características e é usado para armazenar "
                "informações específicas de forma eficiente.")
 
# Exemplo de uso
if __name__ == "__main__":
    data_types = DataTypes()
    print(data_types.structured_data())
    print(data_types.unstructured_data())
    print(data_types.semi_structured_data())
    print(data_types.data_types())
    print(data_types.data_types_description())