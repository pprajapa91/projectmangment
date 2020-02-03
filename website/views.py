from django.shortcuts import render, redirect
from .models import userLogin,addProject,addtask
from .forms import userLoginForm,addProjectdetail,addtaskdetail

# Create your views here.

def login(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        typedata=request.POST.get("is_usertype")


        if username is not None and password is not None and email is not None:
            row = userLogin.objects.filter(username = username, password = password, email = email,is_usertype=typedata)
        
            if len(row)>0:
                if(typedata=="Manager"):
                    request.session["username"]=row[0].username
                    return redirect("http://localhost:8000/manager")
                elif(typedata=="Employee"):
                    request.session["username"]=row[0].username
                    return redirect("http://localhost:8000/employee")

    form = userLoginForm()
    

    return render(request, "login.html", {'form':form})


def manager(request):
    f=addProjectdetail(request.GET)
    
    if f.is_valid():
        temp=f.save(commit=False)
        temp.save()
        return redirect("http://localhost:8000/manager")
    
    form=addProjectdetail()
    

    plist=addProject.objects.all()



    return render(request,'manager.html',{"plist":plist,"form":form})
def employee(request):
    return render(request,'employee.html',None)
def home(request):
    return render(request,'index.html',None)
def addtask(request):
    v=addtaskdetail(request.GET)
    if v.is_valid():
        temp=v.save(commit=False)
        
        temp.save()
    task=addtaskdetail()

    return render(request,'addtask.html',{"v":task})
def viewdetail(request):
    return render(request,'viewprojectdetail.html',None)
