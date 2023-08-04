from django.shortcuts import render
from django.http import HttpResponse


def calculate(x: int | float, y: int | float) -> int:
    return x + y


# Create your views here.
def say_hello(request):
    result = calculate(1, 3)
    return render(request, "hello.html", {"name": "Jen"})
