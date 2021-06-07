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
        user = User.objects.create_user(username=username, password=password)

    return render(request, "signup.html", {})  # 第三引数にhtmlへ渡す変数定数を書くことができる。
