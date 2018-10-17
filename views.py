import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('''
        <h1>Welcome to my home page!</h1>
        <a href="/blog2">About me</a> <br />
        <a href="/github_api">See my GitHub contributions</a> <br />
    ''')


def about_me(request):
    context = {
        'name': 'Kasheena Walton',
    }
    return render(request, 'blog2.html', context)

def contact_me(request):
    context = {
        'contact': 'Email me',
    }
    return render(request, 'contact2.html', context)
   

def content(request):
    context = { 
        'homepage': 'Welcome to my blog',
    }
    return render(request, 'blog1.html', context)

    
def github_api(request):
    response = requests.get('https://api.github.com/users/kasheenawalton/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)
