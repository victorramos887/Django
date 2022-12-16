from django.shortcuts import render, redirect

# Create your views here.

def cadastro(request):
    # sourcery skip: remove-unnecessary-else, swap-if-else-branches

    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if not nome.strip():
            print('O nome não pode ficarm em branco')
            return redirect('cadastro')

        if not email.strip():
            print('O email não pode ficar em branco')
            return redirect('cadastro')

        if senha != senha2:
            print('a senha não é igual')
            return redirect('cadastro')

        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    return render(request, 'usuarios/login.html')


def dashboard():
    pass


def logout():
    pass