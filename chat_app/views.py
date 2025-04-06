from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView

from .forms import SignUpForm

def frontpage(request):
    return render(request, 'main/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('frontpage')
    else:
        form = SignUpForm()

    return render(request, 'main/signup.html', {'form': form})

class CustomLoginView(LoginView):
    def form_invalid(self, form):
        username = self.request.POST.get("username", "").strip()
        password = self.request.POST.get("password", "").strip()

        if username and password:
            messages.error(self.request, "Usuário ou senha incorretos.")
            
        return super().form_invalid(form)
