from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User


def signupfunc(request):
    # print(request.POST) 送信されたPOSTの中身が見られる
    # この下の記述はあえて仕組みがわかるように書くためのもので本来はもっと便利な書き方がある
    # print(request.POST["username"])  # html内のinputのnameがまんまPOSTの中身になっているので注意！
    # print(request.POST["password"])
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username=username, password=password)
            return render(request, "signup.html", {})

        except IntegrityError:
            return render(request, "signup.html", {"error": "User already existed"})

    return render(request, "signup.html", {})  # 第三引数にhtmlへ渡す変数定数を書くことができる。


def loginfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "login.html", {"context": "logged in!"})
        else:
            return render(request, "login.html", {"context": "not log in!"})
    return render(request, "signup.html", {"error": "get method"})
