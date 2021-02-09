from django.shortcuts import render 
  
# Create your views here. 
def mubi_view(request): 
    # render function takes argument  - request 
    # and return HTML as response
    person= {'firstname': 'Mohamed', 'lastname': 'Mubarak'}
    weather= "Raining"
    context= {'person': person,'weather': weather,}
    return render(request, 'mubi1.html',context) 
