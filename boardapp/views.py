from django.http import HttpResponse
from django.shortcuts import render


def signupfunc(request):
    return render(request, "signup.html", {"some": 100})  # 第三引数にhtmlへ渡す変数定数を書くことができる。
