# Gerenciando dependências com Poetry
# Poetry é uma ferramenta de gerenciamento de dependências e empacotamento para projetos Python.

import subprocess
import os
def check_poetry():
    """Verifica se o Poetry está instalado."""
    try:
        subprocess.run(['poetry', '--version'], check=True)
        print("Poetry está instalado.")
    except subprocess.CalledProcessError:
        print("Poetry não está instalado. Por favor, instale o Poetry.")
        exit(1)
def create_poetry_project(project_name):
    """Cria um novo projeto Poetry."""
    try:
        subprocess.run(['poetry', 'new', project_name], check=True)
        print(f"Projeto '{project_name}' criado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao criar o projeto '{project_name}': {e}")
        exit(1)
def install_package_with_poetry(project_name, package_name):
    """Instala um pacote no projeto Poetry."""
    try:
        subprocess.run(['poetry', 'add', package_name], cwd=project_name, check=True)
        print(f"Pacote '{package_name}' instalado com sucesso no projeto '{project_name}'.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar o pacote '{package_name}' no projeto '{project_name}': {e}")
        exit(1)
def list_installed_packages_with_poetry(project_name):
    """Lista os pacotes instalados no projeto Poetry."""
    try:
        subprocess.run(['poetry', 'show'], cwd=project_name, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao listar pacotes instalados no projeto '{project_name}': {e}")
        exit(1)
def update_package_with_poetry(project_name, package_name):
    """Atualiza um pacote no projeto Poetry."""
    try:
        subprocess.run(['poetry', 'update', package_name], cwd=project_name, check=True)
        print(f"Pacote '{package_name}' atualizado com sucesso no projeto '{project_name}'.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao atualizar o pacote '{package_name}' no projeto '{project_name}': {e}")
        exit(1)
def uninstall_package_with_poetry(project_name, package_name):
    """Desinstala um pacote do projeto Poetry."""
    try:
        subprocess.run(['poetry', 'remove', package_name], cwd=project_name, check=True)
        print(f"Pacote '{package_name}' desinstalado com sucesso do projeto '{project_name}'.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao desinstalar o pacote '{package_name}' do projeto '{project_name}': {e}")
        exit(1)
def show_package_dependencies_with_poetry(project_name, package_name):
    """Mostra as dependências de um pacote no projeto Poetry."""
    try:
        subprocess.run(['poetry', 'show', package_name], cwd=project_name, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao mostrar dependências do pacote '{package_name}' no projeto '{project_name}': {e}")
        exit(1)
# Exemplo de uso
if __name__ == "__main__":
    check_poetry()
    project_name = "meu_projeto_poetry"
    
    # Cria um novo projeto Poetry
    create_poetry_project(project_name)
    
    # Instala o pacote requests no projeto
    install_package_with_poetry(project_name, 'requests')
    
    # Lista os pacotes instalados no projeto
    list_installed_packages_with_poetry(project_name)
    
    # Atualiza o pacote requests no projeto
    update_package_with_poetry(project_name, 'requests')
    
    # Desinstala o pacote requests do projeto
    uninstall_package_with_poetry(project_name, 'requests')
    
    # Mostra as dependências do pacote requests no projeto
    show_package_dependencies_with_poetry(project_name, 'requests')
# Poetry é uma ferramenta de gerenciamento de dependências e empacotamento para projetos Python.
# Ele facilita a criação, o gerenciamento e a distribuição de pacotes Python, além de lidar com dependências de forma eficiente.
# Poetry é amplamente utilizado por desenvolvedores Python para gerenciar projetos de forma organizada e eficiente.
# Ele oferece uma interface de linha de comando intuitiva e recursos avançados, como resolução automática de dependências, criação de ambientes virtuais e geração de arquivos de configuração.
# Poetry é uma excelente escolha para desenvolvedores que desejam um gerenciamento de dependências mais robusto e uma experiência de desenvolvimento mais fluida em projetos Python.