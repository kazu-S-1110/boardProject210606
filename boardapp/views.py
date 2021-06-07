from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User


def signupfunc(request):
    object = User.objects.get(username="super")  # objects.allでUser全員を指定可能
    print(object.date_joined)  # いろんなプロパティを指定ができるよ！
    if request.method == "POST":  # methodを受け取ることが可能
        print("this is post method")
    else:
        print("this is not post method")
    return render(request, "signup.html", {})  # 第三引数にhtmlへ渡す変数定数を書くことができる。
