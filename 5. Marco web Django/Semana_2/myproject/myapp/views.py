from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# def home(response):
#     return HttpResponse("Welcome to little lemon web site!")

# def home(request):
#     path = request.path
#     scheme = request.scheme
#     method = request.method
#     address = request.META['REMOTE_ADDR']
#     user_agent = request.META['HTTP_USER_AGENT']
#     path_info = request.path_info
    
#     response = HttpResponse()
#     response.headers['Age'] = 2

#     msg = f"""<br>
#     <br> Path: {path}
#     <br> Address: {address}
#     <br> Scheme: {scheme}
#     <br> Method: {method}
#     <br> User agent: {user_agent}
#     <br> Path info: {path_info}
#     <br> Response header: {response.headers}
#     """

#     return HttpResponse(msg, content_type='text/html', charset='utf-8')

# def drinks(request, drink_name):
#     items = {
#         'moca':'tipo de cafe',
#         'te':'tipo de bebida',
#         'limonada':'tipo de refresco'
#     }
#     description = items[drink_name]
#     return HttpResponse(f"<h2> {drink_name} </h2>" + description)

# Asignacion de vistas

def home(request):
    return HttpResponse("Welcome to Little Lemon!")

def about(request):
    return HttpResponse("About us")

def menu(request):
    return HttpResponse("Menu for Little Lemon")

def book(request):
    return HttpResponse("Make a booking")