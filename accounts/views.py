from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def view_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("website:home")
        else:
            return redirect("accounts:login")
    context = {}
    return render(request,"accounts/login.html",context)


def logout_view(request):
    logout(request)
    return redirect("accounts:login")