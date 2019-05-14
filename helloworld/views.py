 # helloworld/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from .olxjj import *


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

		
def index(request):

	if request.method == 'POST':
		url = request.POST['link']
		search_type = request.POST['search_type']
		
		if search_type == "words":
			words = request.POST['words'].split(" ")
			html_data=[]
			olx_output=OLXJJ(url).get_links_with_word("or",words)
			
			data=""
			for key in olx_output:
				data+=key+"\n"
				data+=str(olx_output.get(key))+"\n"
				data+="\n\n"
			
			vars = {'data':data}
			return render(request, 'output_word_search.html', vars)
		
		if search_type == "prices":
			data=""
			price_data=OLXJJ(url).get_all_prices()
			for item in price_data:
				data+=item+" : "+str(price_data.get(item))+"\n"
			
			vars = {'data':data}
			return render(request, 'output_word_search.html', vars)
		
		
		
	else: 
		vars={}
		return render(request, 'index.html', vars)