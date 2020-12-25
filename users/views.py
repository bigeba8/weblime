from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegsiterForm, UserUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegsiterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('home')

    else:
        form = UserRegsiterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def settings(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('settings')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
        'title': 'Profile Settings'
    }
    return render(request, 'users/settings.html', context)
