from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')
    
# View para cadastro
def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso!')
            print("Usuário cadastrado com sucesso!")  # Adicionei esta linha
            return redirect('login')
        else:
            messages.error(request, 'Erro ao criar conta. Verifique os dados inseridos.')
            print("Erro na validação do formulário:", form.errors)  # Adicionei esta linha
    else:
        form = UserCreationForm()
    return render(request, 'cadastro.html', {'form': form})
    
# View para login
def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('confirmacao')
        else:
            messages.error(request, 'Credenciais inválidas!')
    return render(request, 'login.html')

def confirmacao(request):
    return render(request, 'confirmacao.html')