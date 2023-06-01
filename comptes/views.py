from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate



User = get_user_model()


# Create your views here.
def signup(request):
    if request.method == 'post':
        #traiter le formulaire
      username = request.post.get('username')
      password = request.post.get('password')
      user = User.objects.create_user(username = username, password = password)

      login(request, user)
      return redirect('index')


    return render(request, "comptes/signup.html")
     


def login_user(request):
   if request.method == 'post':
      #connecter l'utilisateur
      username = request.post.get('username')
      password = request.post.get('password')
      user = authenticate(username = username, password = password)

      if user:
         login(request, user)
         return redirect('index')

   return render(request, "comptes/login.html")
   
       


def logout_user(request):
   logout(request)
   return redirect('index')