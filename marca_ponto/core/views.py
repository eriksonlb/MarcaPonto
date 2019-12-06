from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Colaboradores, User
# Create your views here.

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Login Inválido, Checar dados de acesso')
    return redirect('/login')

@login_required(login_url='/login/')
def index(request):
    return render(request, 'index.html')

def logout_user(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
def cadastro(request):
    """
    Get da rota colaborador/cadastro retorna para o rendera lista de usuarios.
    """
    users = User.objects.all()
    return render(request, 'cadastro.html', {'users':users})

@login_required(login_url='/login/')
def cadastro_colaborador(request):
    nome_completo = request.POST.get('nome_completo')
    numero_registro = request.POST.get('numero_registro')
    cargo = request.POST.get('cargo')
    setor = request.POST.get('setor')
    entrada = request.POST.get('entrada')
    intervalo = request.POST.get('intervalo')
    retorno = request.POST.get('retorno')
    saida = request.POST.get('saida')
    dias = request.POST.get('dias')
    adm = request.POST.get('check-adm')
    if not adm: 
        adm = False
    else:
        adm = True

    print(nome_completo, adm)
    return redirect('/')

@login_required(login_url='/login/')
def marcar_ponto(request):
    colaborador = request.POST.get('get_colaborador')
    dia = request.POST.get('get_dia')
    data = request.POST.get('get_data')
    hora = request.POST.get('get_hora')
    print(f'nome: {colaborador} dia: {dia} data: {data} hora:{hora}')
    return redirect('/colaboradores/lista')
    
    
@login_required(login_url='/login/')
def listar_colaboradores(request):
    colaborador = Colaboradores.objects.filter(ativo=True)
    return render(request, 'colaboradores.html', {'colaborador':colaborador})

@login_required(login_url='/login/')
def suporte(request):
    return render(request, 'suporte.html')

@login_required(login_url='/login/')
def chamado_suporte(request):
    titulo = request.POST.get('colaborador')
    tipo = request.POST.get('tipo')
    descricao = request.POST.get('descricao')
    print(f'titulo: {titulo} tipo: {tipo} descricao:{descricao}')    
    return redirect('/')

@login_required(login_url='/login/')
def consulta(request):
    return render(request, 'consulta.html')

@login_required(login_url='/login/')
def espelho_ponto(request):
    return render(request, 'espelho_ponto.html')
