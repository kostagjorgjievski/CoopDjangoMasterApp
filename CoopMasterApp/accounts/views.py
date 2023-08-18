from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import UserProfile

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed


@user_passes_test(lambda user: user.is_anonymous, login_url='dashboard')
def register(request):


    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        deposit_number = request.POST['deposit_number']

        #Check if Password Matches
        if password == password2:
            if User.objects.filter(username=deposit_number).exists():
                messages.error(request, 'The deposit number that you have chosen is already taken.')
                return redirect('register')

            elif len(deposit_number) != 5 and deposit_number.isnumeric():
                messages.error(request, 'The deposit number must be 5 digits long.')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'The email that you have chosen is already taken.')
                    return redirect('register')
                else:
                        user = User.objects.create_user(username=deposit_number, password=password, email=email, first_name=first_name, last_name=last_name)
                        profile = UserProfile.objects.create(user=user)
                        user.save()
                        messages.success(request, 'Your have succsessfuly registered. You can proceed to log in.')
                        return redirect('_login')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

@user_passes_test(lambda user: user.is_anonymous, login_url='dashboard')
def _login(request):

    def test_func(self):
        return self.request.user.is_anonymous

    if request.method == 'POST':
        # SignIn User Logic
        username = request.POST['deposit_number']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have succsesfuly logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'The password or deposit number that you have entered is not in our system.')
            return redirect('_login')
        
    else:
        return render(request, 'accounts/_login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are signed out')
        return redirect('index')
    else:
        return HttpResponseNotAllowed(['POST'])


@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
    