from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from boardapp.models import BoardModel


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
            return redirect("/list")  # redirectの引数は数種類あり。

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
            return redirect("list")
        else:
            return render(request, "signup.html", {"error": "not logged in"})
    return render(request, "login.html", {})


@login_required  # デコレータを定義する。デコレータとは関数が走る前に走らせるもの。
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, "list.html",
                  {"object_list": object_list})  # object_listというキーでBoardModelのオブジェクトを参照できるよう第三引数に指定。


def logoutfunc(request):
    logout(request)
    return redirect("login")


def detailfunc(request, pk):
    obj = get_object_or_404(BoardModel, pk=pk)
    return render(request, "detail.html", {"obj": obj})


def goodfunc(request, pk):
    obj = BoardModel.objects.get(pk=pk)  # このコードはget_object_or_404と同じ（下位互換）
    obj.good = obj.good + 1
    obj.save()
    return redirect("list")


def readfunc(request, pk):
    obj = get_object_or_404(BoardModel, pk=pk)
    username = request.user.get_username()  # ログインしているユーザの名前をとってくる。
    if username in obj.readtext:
        return redirect("list")
    else:
        obj.read = obj.read + 1
        obj.readtext = obj.readtext + " " + username
        obj.save()
        return redirect("list")
