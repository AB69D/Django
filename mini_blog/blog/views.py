from email.headerregistry import Group
from django.shortcuts import render , HttpResponseRedirect
from .forms import SignupForm , LoginForm, PostForm
from django.contrib  import messages 
from django.contrib.auth import authenticate, login,logout
from .models import post
from django.contrib.auth.models import Group

# Home view
def home(request):
    posts =post.objects.all()
    return render(request, 'blog/home.html' , {'posts':posts})

#About page
def about(request):
    return render(request, 'blog/about.html')

#contact page
def contact(request):
    return render(request, 'blog/contact.html')

#Dashbord page
def dashbord(request):
    if request.user.is_authenticated:
        posts = post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps =  user.groups.all()
        return render(request, 'blog/dashbord.html', {'posts':posts,'full_name':full_name,'groups':gps})
    else:
        return HttpResponseRedirect('/login/')


#logout page
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


#Signup page
def user_signup(request):
    if request.method == "POST" :
      form = SignupForm(request.POST)
      if form.is_valid():
          messages.success(request, 'Congratulations !!  You have become an Author..')
          user = form.save()
          group = Group.objects.get(name='Author')
          user.groups.add(group)
    else:  
      form = SignupForm() 
    return render(request, 'blog/signup.html', {'form': form})


#Llogin page
def user_login(request):
    if not request.user.is_authenticated:       
        if request.method == "POST":
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password = upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login successfully..!!')
                    return HttpResponseRedirect('/dashbord/')
        else:
         form = LoginForm()
         return render(request, 'blog/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashbord/')


#Add new post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save() 
                form=PostForm()
        else:
            form = PostForm()

        return render(request, 'blog/addpost.html' , {'form':form})
    else:
        return HttpResponseRedirect('/login/')
    
#update post
def update_post(request , id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi=post.objects.get(pk=id)
            form = PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')


#delete post
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi=post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashbord/')
        
    else:
        return HttpResponseRedirect('/login/')
