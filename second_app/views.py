from django.shortcuts import render
# from django.http import HttpResponse
from second_app.forms import Fn

def index(request):
    Dic={'insert1':'Help is here my friend'}
    return render(request,'second_app\index.html',context=Dic)

def formsv(request):
    form= Fn()
    if  request.method =='POST':
        form= Fn(request.POST)

    if form.is_valid():
        form.save(commit=True)
        print("first_name: "+ form.cleaned_data['first_name'])
        print("second_name: "+ form.cleaned_data['last_name'])
        print("email: "+ form.cleaned_data['email'])

        return index(request)
    else:
        print('ERROR FORM INVALID')

    return render(request,'second_app\Formsv.html',{'form':form})




# Create your views here.
