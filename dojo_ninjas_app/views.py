from django.shortcuts import render, HttpResponse, redirect
from .models import Dojo, Ninja

def index(request):
    context = {
        "all_dojos": Dojo.objects.all(),
        "all_ninjas": Ninja.objects.all()
        # Ninja.objects.filter(dojo=Dojo.objects.all())
    }
    return render(request,'index.html', context)

def submit_dojo(request):
    if request.method == "POST":
        Dojo.objects.create(
            name = request.POST["name"].title(),
            city = request.POST["city"].title(),
            state = request.POST["state"]
        )        
        return redirect('/')
    else:
        return redirect('/')

def submit_ninja(request):
    if request.method == "POST":
        Ninja.objects.create(
            first_name = request.POST["first_name"].title(),
            last_name = request.POST["last_name"].title(),
            dojo = Dojo.objects.get(id=request.POST['dojo'])
        )        
        return redirect('/')
    else:
        return redirect('/')