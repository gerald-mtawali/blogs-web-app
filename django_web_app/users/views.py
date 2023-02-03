from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm

def register(request): 
    if request.method == 'POST': 
        form = UserRegisterForm(request.POST)
        if form.is_valid(): 
            form.save() # save the new user information 
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, user can now Log In')
            return redirect('login')
    else: 
        form = UserRegisterForm(request.POST)
    return render(request, 'users/register.html', context={'form': form})

"""To restrict access unless logged in, include the 'login_required' decorator provided by django's auth module. """
@login_required
def profile(request): 
    return render(request, template_name='users/profile.html', context={})
