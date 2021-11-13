from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm

def projects(request):
    projct_obj = Project.objects.all()
    context = {
        'projects':projct_obj,
    }
    return render(request, 'projects/projects.html',context)

def single_project(request,pk):
    project = Project.objects.get(id=pk)

    context = {'project':project}

    return render(request, "projects/single_project.html", context)

@login_required(login_url='login')    
def create_project(request):
    form = ProjectForm()

    if request.method=="POST":
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            context = {
                'form':form
            }
            return redirect('projects')
    elif request.method=="GET":
        context = {
                'form':form
            }
        return render(request,"projects/add_project.html",context)

@login_required(login_url='login')
def update_project(request,pk):

    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES, instance=project)

        if form.is_valid():
            form.save()
            return redirect('projects')
    
    
    context = {'form':form}
    return render(request, 'projects/add_project.html', context)

@login_required(login_url='login')
def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    
    if request.method == 'POST':

        project.delete()
        return redirect('projects')
    else:
        context = {
            'project':project
        }
        return render(request,"projects/delete_project.html", context)







