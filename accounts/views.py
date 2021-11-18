from django.shortcuts import render, redirect
from .forms import UserAdminCreationForm
from django.contrib.auth import login, authenticate

def signup(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('exam_list')
    else:
            form = UserAdminCreationForm()
    return render(request, 'registration/signup.html', {'form': form})