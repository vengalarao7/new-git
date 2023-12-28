from django.shortcuts import render, redirect

from django.shortcuts import render

from .models import Login

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        Login.objects.create(username=username, password=password)

        return redirect('registration_success')

    return render(request, 'registration.html')



def registration_success(request):
    return render(request, 'registration_success.html')
