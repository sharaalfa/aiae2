from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

def home(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()

    return render(request, "home.html", {
        'form': form
    })

def handle_uploaded_file(file):
    pass