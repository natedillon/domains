from django.http import HttpResponse
from django.shortcuts import render
import pythonwhois


def home(request, **kwargs):

    # Initialize the context
    context = {}

    # Check for query
    if request.method == 'GET' and 'q' in request.GET:

        # Set the query value
        context['query'] = request.GET['q']

        # Set the domain name
        name = context['query']

        # Create the domain context
        context['domain'] = {
            'name': name,
            'whois': pythonwhois.get_whois(name),
        }

    return render(request, 'domains/index.html', context)
