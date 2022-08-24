from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from . import models
# Create your views here.
def home(request):
    return render(request, "base.html")

Base_Craigslist_URL = 'https://losangeles.craigslist.org/d/services/search/bbb?query={}'
def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search= search)
    final_URL = Base_Craigslist_URL.format(quote_plus(search))
    response = requests.get(final_URL)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_listing = soup.find_all('li',{'class':'result-row'})
    post_title = post_listing[0].find(class_= 'result-title').text
    print(post_title)
    return render(request, "my_app/new_search.html", {'search' : search} )