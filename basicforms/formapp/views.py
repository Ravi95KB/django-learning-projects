from django.shortcuts import render
from formapp.forms import FormName
# Create your views here.

def index(request):
    return render(request,'formapp/index.html')

def form_name_view(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            print("Name: "+form.cleaned_data['name'])      #Syntax to grab the data from the form webpage input.
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])

    return render(request,'formapp/form_page.html',context={'form':form})
