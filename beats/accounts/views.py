from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.db import IntegrityError 

CustomUser = get_user_model()

class SignUpView(CreateView):
    model = CustomUser
    
    template_name = 'accounts/signup.html'
    
    success_url = reverse_lazy('login') 

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not all([username, email, password, password2]):
            error_msg = 'Todos os campos são obrigatórios.'
            context = {'error': error_msg, 'username': username, 'email': email}
            return render(request, self.template_name, context)

        if password != password2:
            error_msg = 'As senhas não coincidem.'
            context = {'error': error_msg, 'username': username, 'email': email}
            return render(request, self.template_name, context)

        try:
            CustomUser.objects.create_user(
                username=username, 
                email=email, 
                password=password
            )
            return redirect(self.success_url)

        except IntegrityError:
            error_msg = "Este nome de usuário ou e-mail já está em uso."
            context = {'error': error_msg, 'username': username, 'email': email}
            return render(request, self.template_name, context)
            
        except Exception as e:
            error_msg = f'Ocorreu um erro ao tentar cadastrar: {e}'
            context = {'error': error_msg, 'username': username, 'email': email}
            return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)