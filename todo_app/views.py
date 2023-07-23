from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


from .models import todo_app




def index(request):
    if request.method == 'POST':
        uname= request.POST.get("username")
        pass1 = request.POST.get("pass")
        user = authenticate(request,username=uname,password =pass1)


        if user is not None:
            login(request,user)
            return redirect("home")
        
        else:
            return HttpResponse("username or password is wrong!")
        

    return render(request,"todo_app/index.html")

@login_required(login_url='index')
def home(request):
    if request.method == "POST":
        

        title = request.POST.get("head")
        info = request.POST.get("message")
        print(title,info)

        t=todo_app()
        t.head = title
        t.message = info

        t.save()

    datas = todo_app.objects.all()

        





    return render(request,"todo_app/home.html",{"datas":datas})

