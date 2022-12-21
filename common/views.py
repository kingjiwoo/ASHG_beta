from django.shortcuts import render, redirect
from django.contrib import auth, messages



# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST': 
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            if user.division == '매니저':
                return redirect('manager:list')
            elif user.division == '업소':
                return redirect('lodge:list')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('common:login')
            
    