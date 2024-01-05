from django.http import HttpResponse

def handle404(request, exception):
    return HttpResponse("404 Page not found!")