from django.shortcuts import render
import pythonwhois

def home(request):

    # Initialize the context
    context = {}

    # Set the domain name
    name = 'natedillon.com'

    # Create the domain context
    context['domain'] = {
        'name': name,
        'whois': pythonwhois.get_whois(name),
    }

    return render(request, 'domains/index.html', context)
