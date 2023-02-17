from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm

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
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user) # user update form
        # perform update of user profile image, the additional argument 'request.FILES' is included 
        # to handle the image file being uploaded
        p_form = ProfileUpdateForm(request.POST, request.FILES, 
                                   instance=request.user.profile) 
        # confirm that both the user info form is valid and the profile form is valid
        if u_form.is_valid() and p_form.is_valid(): 
            u_form.save()
            p_form.save()
            # provide a success response to the user
            messages.success(request, f'Account successfully updated!!')
            # perform a redirect to avoid the POST GET Redirect Pattern issue
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user) # user update form
        p_form = ProfileUpdateForm(instance=request.user.profile) # profile image update form 
        
    context = {
        'u_form': u_form, 
        'p_form': p_form
    }
    return render(request, template_name='users/profile.html', context=context)


