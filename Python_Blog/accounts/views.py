from django.forms import ValidationError
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate,login

from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import CustomUserCreationForm

from .models import Post
from django.views import generic

from django.contrib.auth.decorators import login_required
import base64

# Create your views here.

@login_required(login_url="/accounts/login/")  
def dashboard(request): 
    if request.method == 'GET':                
        current_user = request.user 
       
        if current_user is not None:         
            posts = Post.objects.filter(user=current_user) 
           
            for post in posts:
                if post.image1 is not None:
                    #post.image1 = base64.b64decode(post.image1)
                    post.image1 = base64.b64encode(post.image1).decode('utf-8')                              
            context = { 'posts': posts }
            return render(request, 'accounts/Post-list.html', context)
        else:
             return reverse("/accounts/login/")

def add_post(request):    
    if request.method == 'POST': 
        current_user = request.user
        if current_user is not None:
            title = request.POST['title']
            description = request.POST['description']
            details = request.POST['details']           
            image1 = request.FILES['image']           
            
            file_extension =image1.name.split('.')[1].lower()
            allowed_extensions = ['png', 'jpeg', 'jpg']
    
            # Validating File extension
            if file_extension in allowed_extensions:
                binary_image = image1.read()             
            else:
                return render(
                    request, "accounts/add-post.html" , { "Message" : "Uploaded file format is not supported" }
                )
            
            #Validating image size
            if (image1.size > 2 * 1024 * 1024):
                return render(
                    request, "accounts/add-post.html" , { "Message" : "Uploaded file size exceeded the limit" }
                )
                                          
            post = Post.objects.create(title=title, description=description,details=details, image=image1, image1=binary_image, user=current_user)
            post.save()            
            return render(
                request, "accounts/add-post.html", { "Message" : "Post saved Successfully" }
            )
        
        else:
             return reverse("/accounts/login/")
            
    
    if request.method == 'GET': 
        return render(
            request, "accounts/add-post.html"
        )
    
def register(request):
    if request.method == "GET":
        return render(
            request, "accounts/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":        
        form = CustomUserCreationForm(request.POST)        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))


def post_list(request):
    if request.method == "GET": 
        current_user = request.user
        if current_user is not None:            
            posts = Post.objects.filter(user=current_user)  
            context = { 'posts': posts }          
            return render(
                request, "accounts/post-list.html", context
            )  
            
