from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request,'djan_app/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("This is it")
            print("Name:"+form.cleaned_data['name'])
            print("Email:"+form.cleaned_data['email'])
            print("Text:"+form.cleaned_data['text'])

    return render(request, 'djan_app/form_page.html',{'form':form})
