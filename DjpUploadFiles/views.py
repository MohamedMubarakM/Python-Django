from django.shortcuts import render, HttpResponse
import os

def home(request):
    return render(request, 'index.html', {'header':'Django File Upload'})

def upload(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse('Upload successful!')
    return HttpResponse('Upload failed')
    
def handle_uploaded_file(file, filename):
    if not os.path.exists('DjpUploadFiles/uploaded_files/'):
        os.mkdir('DjpUploadFiles/uploaded_files/')
    with open('DjpUploadFiles/uploaded_files/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

