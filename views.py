from django.shortcuts import render 
  
# Create your views here. 
def mubi_view1(request): 
    return render(request, 'mubiOne.html')
def mubi_view2(request):
    return render(request, 'mubiTwo.html') 
