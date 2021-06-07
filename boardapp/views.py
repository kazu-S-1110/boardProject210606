from django.http import HttpResponse
from django.shortcuts import render


def signupfunc(request):
    if request.method == "POST":  # methodを受け取ることが可能
        print("this is post method")
    else:
        print("this is not post method")
    return render(request, "signup.html", {})  # 第三引数にhtmlへ渡す変数定数を書くことができる。
