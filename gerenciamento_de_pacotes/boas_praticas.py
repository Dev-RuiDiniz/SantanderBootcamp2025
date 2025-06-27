# Boas praticas para gerenciamento de pacotes
# 1. Use um arquivo de bloqueio (lock file) para garantir que as versões das dependências sejam consistentes entre diferentes ambientes.
# 2. Mantenha suas dependências atualizadas regularmente para evitar problemas de segurança e compatibilidade.
# 3. Use ambientes virtuais para isolar as dependências do seu projeto e evitar conflitos com outras bibliotecas instaladas globalmente.
# 4. Documente as dependências do seu projeto em um arquivo README ou em outro local apropriado, para que outros desenvolvedores possam entender facilmente quais pacotes são necessários.
# 5. Evite instalar pacotes desnecessários ou redundantes, para manter o projeto leve e fácil de manter.
# 6. Use ferramentas de análise de dependências para identificar e remover pacotes não utilizados ou obsoletos.
# 7. Teste seu projeto regularmente para garantir que as dependências estejam funcionando corretamente e que não haja conflitos entre elas.

import subprocess
def check_poetry():
    """Verifica se o Poetry está instalado."""
    try:
        subprocess.run(['poetry', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Poetry está instalado.")
    except subprocess.CalledProcessError:
        print("Poetry não está instalado. Por favor, instale o Poetry antes de continuar.")
        exit(1)
def create_poetry_project(project_name):
    """Cria um novo projeto Poetry."""
    try:
        subprocess.run(['poetry', 'new', project_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Projeto '{project_name}' criado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao criar o projeto '{project_name}': {e}")
        exit(1)
def install_package_with_poetry(project_name, package_name):
    """Instala um pacote no projeto Poetry."""
    try:
        subprocess.run(['poetry', 'add', package_name], cwd=project_name, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Pacote '{package_name}' instalado com sucesso no projeto '{project_name}'.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar o pacote '{package_name}' no projeto '{project_name}': {e}")
        exit(1)
def list_installed_packages_with_poetry(project_name):
    """Lista os pacotes instalados no projeto Poetry."""
    try:
        subprocess.run(['poetry', 'show'], cwd=project_name, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao listar pacotes instalados no projeto '{project_name}': {e}")
        exit(1)
def update_package_with_poetry(project_name, package_name):
    """Atualiza um pacote no projeto Poetry."""
    try:
        subprocess.run(['poetry', 'update', package_name], cwd=project_name, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Pacote '{package_name}' atualizado com sucesso no projeto '{project_name}'.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao atualizar o pacote '{package_name}' no projeto '{project_name}': {e}")
        exit(1)
        
        