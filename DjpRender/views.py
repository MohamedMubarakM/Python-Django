from django.shortcuts import render 
  
# Create your views here. 
def mubi_view(request): 
    # render function takes argument  - request 
    # and return HTML as response 
    return render(request, "mubi.html") 
