from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Hello DevOps! A fresh start yooo.</h1>")