from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import contacts
from django.core.mail import send_mail

# Create your views here.
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password ==  confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists")
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name = firstname,
                                                    last_name = lastname,
                                                    username = username,
                                                    email = email,
                                                    password = password)
                    user.save()
                    messages.success(request, "User successfully registered !!")
                    return redirect('login')
        else:
            messages.error(request, "Password does not match")
            return redirect('register')
        
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now successfully logged in")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'accounts/login.html')

def dashboard(request):
    if request.user.is_authenticated:
        contact = contacts.objects.filter(user_id=request.user.id)
        context = {
            'contacts': contacts,
        }
        return render(request, 'accounts/dashboard.html', context=context)

def logout(request):
    auth.logout(request)
    messages.success(request, "You are successfully logged out!! ")
    return redirect('login')