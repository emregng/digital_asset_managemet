from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

from .forms import CreateUserForm
from .decorators import unauthenticated_user
from media.models import Customer

# Create your views here.


@unauthenticated_user
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
    return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("accounts:login")


@unauthenticated_user
def view_register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            group = Group.objects.get(name='admin')
            user.groups.add(group)

            Customer.objects.create(
                user=user,
            )

            return redirect('accounts:login')

    context = {'form': form}
    return render(request, "accounts/register.html", context)


@login_required(redirect_field_name='accounts:login')
def accountSettings(request):
    user = request.user
    form = CreateUserForm(instance=user)

    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'accounts/settings.html', context)
