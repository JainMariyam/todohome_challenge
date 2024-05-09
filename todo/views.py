from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View,CreateView,FormView,ListView,DetailView
from todo.forms import UserCreationForm,UserForm,LoginForm,ProjectForm,TodoForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from todo.models import Project,Todo
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator

# Create your views here.


def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('signin')
        else:
            return fn(request,*args,**kwargs)
    return wrapper



class SignUpView(CreateView):
   template_name="register.html"
   form_class=UserForm
   
   def get_success_url(self):
      return reverse('signup')
  
  
class signInView(FormView): 
   template_name="login.html"
   form_class=LoginForm
   
   def post(self,request,*args,**kwargs):
      form=LoginForm(request.POST)
      if form.is_valid():
         uname=form.cleaned_data.get("username")
         pwd=form.cleaned_data.get("password")
         user_object=authenticate(request,username=uname,password=pwd)
         if user_object:
            login(request,user_object)
            print("valid")
            return redirect('index')     
      else:
            print("invalid")
            return render(request,"login.html",{"form":form})  


@method_decorator(signin_required,name="dispatch") 
class IndexView(View): 
    def get(self,request,*args,**kwargs):
        qs=Project.objects.filter(user=request.user)
        print(qs)
        form=ProjectForm()
        return render(request,'index.html',{'data': qs, 'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('index')
        else:
            print(form.errors)
            return render(request, "index.html", {'form': form})
        
@method_decorator(signin_required,name="dispatch") 
class ProjectView(DetailView):
    template_name="project_detail.html"
    model=Project
    context_object_name="data" 
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_form'] = TodoForm()  
        return context

    def post(self, request, *args, **kwargs):
        project = self.get_object()  
        todo_form = TodoForm(request.POST)  
        if todo_form.is_valid():
            todo = todo_form.save(commit=False)
            todo.user = request.user
            todo.project = project  
            todo.title=project.title
            todo.save() 
            return HttpResponseRedirect(reverse('project-detail', kwargs={'pk': project.pk}))
        else:
            return self.render_to_response(self.get_context_data(todo_form=todo_form))
    
    def update_todo(request):
        if request.method == 'POST':
            todo_id = request.POST.get('todo_id')
            todo = get_object_or_404(Todo, pk=todo_id)
            todo.name = request.POST.get('name')
            todo.description = request.POST.get('description')
            todo.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@method_decorator(signin_required,name="dispatch")    
class ProjectDeleteView(View):
    def get(self, request, *args, **kwargs):
        project_id = kwargs.get('pk')
        project = Project.objects.get(id=project_id)
        project.delete()
        return redirect('index') 
    
@method_decorator(signin_required,name="dispatch") 
class TodoDeleteView(View):
    def get(self, request, *args, **kwargs):
        todo_id = kwargs.get('pk')
        todo = Todo.objects.get(id=todo_id)
        project_pk = todo.project.pk
        todo.delete()
        return redirect('project-detail', pk=project_pk)
  
@method_decorator(signin_required,name="dispatch") 
class TodoStatusView(View):
    def post(self, request, *args, **kwargs):
        todo_id = kwargs.get('pk')
        todo = Todo.objects.get(id=todo_id)
        if todo.status == 'pending':
            todo.status = 'completed'
        else:
            todo.status = 'pending'
        todo.save()
        return redirect('project-detail', pk=todo.project.pk)

@method_decorator(signin_required,name="dispatch") 
class UpdateTodoView(View): 
    def post(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        todo.name = request.POST.get('name', '')
        todo.description = request.POST.get('description', '')
        todo.save()
        return redirect('project-detail', pk=todo.project_id)
   
@method_decorator(signin_required,name="dispatch")  
class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('signin')    

@method_decorator(signin_required,name="dispatch")  
class ProjectTitleView(View):
     def post(self, request, *args, **kwargs):
        project_id = kwargs.get('pk')
        project = get_object_or_404(Project, pk=project_id)
        new_title = request.POST.get('title')
        project.title = new_title
        project.save() 
        return redirect("index") 