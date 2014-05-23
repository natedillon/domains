from django.shortcuts import render
import pythonwhois

def home(request):

    context = {}

    context['domain'] = pythonwhois.get_whois('google.com')

    return render(request, 'domains/index.html', context)
