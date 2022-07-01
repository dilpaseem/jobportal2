from django.shortcuts import render

# Create your views here.
def user_login(request):
    return render(request,'jobadmin/login.html')
def employers_view(request):
    return render(request,'jobadmin/employers.html')