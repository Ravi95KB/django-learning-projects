from django.shortcuts import render
# from django.http import HttpResponse
#from AppTwo.models import User
from AppTwo.forms import NewUserForm
# Create your views here.

def index(request):
    #return HttpResponse("<em>My Second App</em>")
    return render(request,'AppTwo/index.html')

# def help(request):
#     helpdict = {'help_insert':"HELP PAGE"}
#     return render(request,'AppTwo/help.html',context=helpdict)

def users(request):
    # name_list = User.objects.order_by('first_name')
    # name_dict = {'name_records':name_list}
    # return render(request,'AppTwo/users.html',context=name_dict)

    form  = NewUserForm()

    if request.method == "POST":
        form  = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)      #To save it to database.
            return index(request)
        else:
            print("ERROR FORM INVALID")

    return render(request,'AppTwo/users.html',{'form':form})
