from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # pentru mesaje de succes/eroare

from products.models import Order
from .forms import UserProfileForm
from .models import UserProfile


# 🔹 Înregistrare utilizator nou
def register(request):
    if request.method == 'POST':
        print("✅ Cerere POST primită!")  # Debug temporar
        print("Date trimise:", request.POST)

        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Creează automat profilul
            UserProfile.objects.create(user=user)

            # Autentifică utilizatorul
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'])
            if user:
                login(request, user)
                messages.success(request, "Contul a fost creat cu succes!")
                return redirect('dashboard')
        else:
            messages.error(request, "Formular invalid. Verifică datele.")
    else:
        form = UserCreationForm()

    return render(request, 'account/register.html', {'form': form})


# 🔹 Dashboard cu comenzile recente
@login_required
def dashboard_view(request):
    recent_orders = Order.objects.filter(user=request.user).order_by('-created_at')[:5]

    context = {
        'recent_orders': recent_orders,
    }
    return render(request, 'account/dashboard.html', context)


# 🔹 Logout utilizator
def logout_view(request):
    logout(request)
    return redirect('login')


# 🔹 Login personalizat
def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})



# 🔹 Editare profil
@login_required
def profile_view(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profilul a fost salvat cu succes!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'account/profile.html', {'form': form})
