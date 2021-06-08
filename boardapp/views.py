from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
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
            return redirect("/list") # redirectの引数は数種類あり。

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
            return render(request, "list.html", {})
        else:
            return render(request, "list.html", {})
    return render(request, "login.html", {"error": "get method"})


def listfunc(request):
    return render(request, "list.html", {})