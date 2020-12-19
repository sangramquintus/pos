from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "home/index.html")


def dashboard(request):
    return render(request, "dashboard/index.html")


def logout(request):
    return render(request, 'home/index.html')

def login_redirect(request):
    login_status = request.GET.get("status")
    request_token = request.GET.get("request_token")
    return render(request, 'home/index.html', {"request_token" : request_token, "login_status" : login_status})
