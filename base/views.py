from django.shortcuts import render
import requests
from .models import Topic, Item

# Create your views here.
def home(request):

    return render(request, 'index.html')


def not_built(request):
    return render(request,'not_built.html')

def menu(request):

    topics = Topic.objects.all()
    context = {
        'topics': topics
    }

    return render(request,'menu.html', context)

def fal_hafez(request):

    url = "https://hafez.p.rapidapi.com/fal"

    headers = {
        "x-rapidapi-key": "e4a0ededcbmsh5107e99acdaea5ap14c962jsn4895b1e2ecf7",
        "x-rapidapi-host": "hafez.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

        # Extract 'poem' and 'text' from the response
    poem_number = data.get('id')
    poem = data.get('poem')
    text = data.get('text')

    # Pass the extracted data to the template context
    context = {
        'poem': poem,
        'text': text,
        'poem_number': poem_number,
    }

    return render(request,'fal_hafez.html', context)