# Gerenciando dependências com Pipenv
# Pipenv é uma ferramenta que combina o gerenciamento de pacotes e ambientes virtuais, facilitando o processo de desenvolvimento em Python. Ele cria um ambiente virtual isolado para cada projeto e gerencia as dependências de forma eficiente.
import subprocess
import os
import sys
# Verifica se o Pipenv está instalado
def check_pipenv():
    try:
        subprocess.run(['pipenv', '--version'], check=True)
        print("Pipenv está instalado.")
    except subprocess.CalledProcessError:
        print("Pipenv não está instalado. Por favor, instale o Pipenv.")
        sys.exit(1)
# Verifica se o Pipenv está instalado
check_pipenv()

# Criação de um ambiente virtual com Pipenv
def create_virtual_environment():
    try:
        subprocess.run(['pipenv', 'install'], check=True)
        print("Ambiente virtual criado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao criar o ambiente virtual: {e}")
        sys.exit(1)
# Cria um ambiente virtual se não existir
if not os.path.exists('Pipfile'):
    create_virtual_environment()
# Instalação de pacotes com Pipenv
def install_package_with_pipenv(package_name):
    try:
        subprocess.run(['pipenv', 'install', package_name], check=True)
        print(f"Pacote '{package_name}' instalado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar o pacote '{package_name}': {e}")
# Exemplo de instalação do pacote requests com Pipenv
install_package_with_pipenv('requests')
# Listagem de pacotes instalados com Pipenv
def list_installed_packages_with_pipenv():
    try:
        subprocess.run(['pipenv', 'graph'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao listar pacotes instalados: {e}")
# Exemplo de listagem de pacotes instalados com Pipenv
list_installed_packages_with_pipenv()
# Atualização de pacotes com Pipenv
def update_package_with_pipenv(package_name):
    try:
        subprocess.run(['pipenv', 'update', package_name], check=True)
        print(f"Pacote '{package_name}' atualizado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao atualizar o pacote '{package_name}': {e}")
# Exemplo de atualização do pacote requests com Pipenv
update_package_with_pipenv('requests')
# Desinstalação de pacotes com Pipenv  
def uninstall_package_with_pipenv(package_name):
    try:
        subprocess.run(['pipenv', 'uninstall', package_name], check=True)
        print(f"Pacote '{package_name}' desinstalado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao desinstalar o pacote '{package_name}': {e}")
# Exemplo de desinstalação do pacote requests com Pipenv
uninstall_package_with_pipenv('requests')
# Verificação de dependências com Pipenv
def show_package_dependencies_with_pipenv(package_name):
    try:
        subprocess.run(['pipenv', 'run', 'pip', 'show', package_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao mostrar dependências do pacote '{package_name}': {e}")
# Exemplo de verificação de dependências do pacote requests com Pipenv
show_package_dependencies_with_pipenv('requests')
# Uso de Pipfile e Pipfile.lock
# O Pipenv utiliza o Pipfile para gerenciar as dependências do projeto e o Pipfile.lock para garantir que as versões das dependências sejam consistentes entre diferentes ambientes. O Pipfile contém as dependências do projeto, enquanto o Pipfile.lock registra as versões exatas instaladas.
# O Pipfile é criado automaticamente quando você instala um pacote com Pipenv, e o Pipfile.lock é atualizado para refletir as versões exatas dos pacotes instalados. Você pode visualizar o conteúdo do Pipfile e do Pipfile.lock para entender melhor as dependências do seu projeto.
# Exemplo de visualização do Pipfile
def view_pipfile():
    try:
        with open('Pipfile', 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("Pipfile não encontrado. Certifique-se de que o ambiente virtual foi criado.")
    except Exception as e:
        print(f"Erro ao ler o Pipfile: {e}")
view_pipfile()
# Exemplo de visualização do Pipfile.lock
def view_pipfile_lock():
    try:
        with open('Pipfile.lock', 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("Pipfile.lock não encontrado. Certifique-se de que o ambiente virtual foi criado e os pacotes foram instalados.")
    except Exception as e:
        print(f"Erro ao ler o Pipfile.lock: {e}")
view_pipfile_lock()
# Exemplo de uso do Pipenv para rodar scripts
def run_script_with_pipenv(script_name):
    try:
        subprocess.run(['pipenv', 'run', script_name], check=True)
        print(f"Script '{script_name}' executado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o script '{script_name}': {e}")
# Exemplo de execução de um script Python com Pipenv
run_script_with_pipenv('python script.py')  # Substitua 'script.py' pelo nome do seu script
# Conclusão
# O Pipenv é uma ferramenta poderosa para gerenciar pacotes e ambientes virtuais em projetos Python. Ele simplifica o processo de instalação, atualização e desinstalação de pacotes, além de garantir que as dependências sejam gerenciadas de forma eficiente. Com o Pipenv, você pode facilmente criar ambientes isolados para cada projeto, evitando conflitos entre pacotes e versões.
# É recomendável utilizar o Pipenv para projetos Python, especialmente quando se trabalha com múltiplos pacotes e dependências. Para mais informações, consulte a documentação oficial do Pipenv: https://pipenv.pypa.io/en/latest/
# Certifique-se de executar esses comandos em um ambiente Python adequado, como um ambiente virtual, para evitar conflitos com pacotes globais. O Pipenv facilita a criação e o gerenciamento desses ambientes, tornando o desenvolvimento em Python mais organizado e eficiente.
# Certifique-se de que o Pipenv está instalado e configurado corretamente antes de executar os comandos. Você pode instalar o Pipenv usando o seguinte comando:
# pip install pipenv 