from django.shortcuts import render

# Create your views here.

def user_login(request):
    return render(request,'jobseekers/login.html')
def search_job(request):
    return render(request,'jobseekers/jobsearch.html')
def details_job(request):
    return render(request,'jobseekers/jobdetails.html')

