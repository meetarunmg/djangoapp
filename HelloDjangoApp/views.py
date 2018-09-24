from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def index(request):
	now = datetime.now()

	return render(
        request,
        "index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title' : "Hello Django",
            'message' : "Hello Django!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

    #html_content = "<html><head><title>Hello, Django</title></head><body>"
    #html_content += "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
    #html_content += "</body></html>"

    #return HttpResponse(html_content)
def about(request):
    return render(
        request,
        "about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )