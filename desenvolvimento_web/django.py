# Django Framework:
# Django é um framework web de alto nível para desenvolvimento de aplicações web em Python. Ele segue o padrão de arquitetura Model-View-Template (MVT) e oferece uma série de recursos que facilitam o desenvolvimento, como um ORM (Object-Relational Mapping) para interação com bancos de dados, sistema de autenticação, administração automática e suporte a testes.
# # Django é conhecido por sua segurança, escalabilidade e facilidade de uso, tornando-o uma escolha popular para desenvolvedores que desejam criar aplicações web robustas e eficientes. Ele também possui uma comunidade ativa e uma vasta gama de pacotes e extensões que podem ser facilmente integrados às aplicações.

#Exemplo de uso do Django:
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
class HelloWorldView(View):
    """Exemplo de view simples no Django que retorna uma resposta HTTP."""
    
    def get(self, request):
        """Método GET que retorna uma resposta simples."""
        return HttpResponse("Hello, World!")
# Exemplo de uso do Django com templates:
def home(request):
    """Exemplo de view que renderiza um template HTML."""
    context = {
        'message': 'Bem-vindo ao Django!'
    }
    return render(request, 'home.html', context)
# Exemplo de uso do Django com modelos:
from django.db import models
class Product(models.Model):
    """Modelo de produto no Django."""
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        """Retorna uma representação em string do produto."""
        return self.name
# Exemplo de uso do Django com formulários:
from django import forms
class ContactForm(forms.Form):
    """Exemplo de formulário de contato no Django."""
    name = forms.CharField(max_length=100, label='Seu Nome')
    email = forms.EmailField(label='Seu Email')
    message = forms.CharField(widget=forms.Textarea, label='Sua Mensagem')
    
    def clean_message(self):
        """Validação personalizada para o campo de mensagem."""
        data = self.cleaned_data['message']
        if len(data) < 10:
            raise forms.ValidationError("A mensagem deve ter pelo menos 10 caracteres.")
        return data
# Exemplo de uso do Django com autenticação:
from django.contrib.auth import authenticate, login, logout
def user_login(request):
    """Exemplo de view para autenticação de usuário no Django."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Login bem-sucedido!")
        else:
            return HttpResponse("Credenciais inválidas.")
    return render(request, 'login.html')
def user_logout(request):
    """Exemplo de view para logout de usuário no Django."""
    logout(request)
    return HttpResponse("Logout realizado com sucesso!")
# Exemplo de uso do Django com rotas:
from django.urls import path
urlpatterns = [
    path('', HelloWorldView.as_view(), name='hello_world'),
    path('home/', home, name='home'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
]
# Exemplo de uso do Django com testes:
from django.test import TestCase
class ProductModelTest(TestCase):
    """Exemplo de teste de modelo no Django."""
    
    def setUp(self):
        """Configuração inicial do teste."""
        self.product = Product.objects.create(name='Produto Teste', price=19.99)
    
    def test_product_str(self):
        """Teste da representação em string do modelo Product."""
        self.assertEqual(str(self.product), 'Produto Teste')
    
    def test_product_price(self):
        """Teste do preço do produto."""
        self.assertEqual(self.product.price, 19.99)
# Exemplo de uso do Django com administração:
from django.contrib import admin
from .models import Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Exemplo de configuração de administração para o modelo Product."""
    list_display = ('name', 'price')
    search_fields = ('name',)
    list_filter = ('price',)
# Exemplo de uso do Django com middleware:
from django.utils.deprecation import MiddlewareMixin
class CustomMiddleware(MiddlewareMixin):
    """Exemplo de middleware personalizado no Django."""
    
    def process_request(self, request):
        """Método chamado para processar a requisição antes de chegar à view."""
        print("Requisição recebida:", request.path)
    
    def process_response(self, request, response):
        """Método chamado para processar a resposta antes de ser enviada ao cliente."""
        print("Resposta enviada:", response.status_code)
        return response
# Exemplo de uso do Django com cache:
from django.core.cache import cache
def cached_view(request):
    """Exemplo de view que utiliza cache no Django."""
    cached_data = cache.get('cached_data')
    if not cached_data:
        # Simula uma operação cara, como uma consulta ao banco de dados
        cached_data = "Dados caros para calcular"
        cache.set('cached_data', cached_data, timeout=60)  # Cache por 60 segundos
    return HttpResponse(cached_data)
# Exemplo de uso do Django com WebSockets:
# from channels.generic.websocket import AsyncWebsocketConsumer 
# class ChatConsumer(AsyncWebsocketConsumer):
#     """Exemplo de consumidor WebSocket no Django Channels."""
#     async def connect(self):
#         """Método chamado quando a conexão WebSocket é estabelecida."""
#         await self.accept()
#     async def disconnect(self, close_code):
#         """Método chamado quando a conexão WebSocket é fechada."""
#         pass
#     async def receive(self, text_data):
#         """Método chamado quando uma mensagem é recebida pelo WebSocket."""
#         await self.send(text_data="Mensagem recebida: " + text_data)
