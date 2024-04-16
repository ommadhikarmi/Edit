from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Todo
# Create your views here.
def home(request):
    todo_objects = Todo.objects.all()   # to query database (ORM query)-Object Relation Manager 'all' method which shows Todo table all data  
    content = {'todo':todo_objects} # use dictanary format not directly 
    return render(request,'create.html',context=content)

def form(request):
    if request.method == 'POST':
       # print(request.POST.get('name'))
        name = request.POST.get('name')
        discription = request.POST.get('discription')
        status = request.POST.get('status')
        Todo.objects.create(name = name,discription = discription,status = status)
        return redirect('home')   
    return render(request,'form.html')

def edit(request,pk):
   
    todo_objects = Todo.objects.get(id=pk)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        new_discription = request.POST.get('discription')
        new_status = request.POST.get('status')
        todo_objects.name = new_name
        todo_objects.discription = new_discription
        todo_objects.status = new_status        
        todo_objects.save() 
        return redirect('home') 
         
    content = {'todo':todo_objects}       
    return render(request,'edit.html',context=content)