from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm

def loginPage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try :
            user = User.ojects.get(username=username)
        except:
            messages.error(request, 'user does not exist ')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'user/password didnt match')
            return render(request,'users/login_register.html')
    return render(request,'users/login_register.html')

def registerUser(request):
    page='register'
    form = CustomUserCreationForm()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User accont was created")
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Error has occurred.")

    context = {'page':page,'form':form}
    return render(request, 'users/login_register.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def profiles(request):
    profile = Profile.objects.all()
    context = {'profiles':profile}
    return render(request, 'users/profile.html',context)

def user_profile(request,pk):
    profile = Profile.objects.get(id=pk)
    print("PROFILE",profile)
    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description__exact="")

    context = {
        'profile':profile,
        'top_skills':top_skills,
        'other_skills':other_skills
    }
    return render(request, "users/user_profile.html",context)