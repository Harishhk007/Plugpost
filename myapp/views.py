from django.shortcuts import render
from .models import Users
from .models import Blogs
from .forms import Usersform
from .forms import Blogform
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request,"home.html")
def lhome(request):
    your_blog = Blogs.objects.all().order_by('-Blog_id')
    return render(request,"LHOME.html",{'yours':your_blog})
def login(request):
    if request.method == 'POST':
        user = request.POST.get('loguser')
        pass1 = request.POST.get('logpas')
        
        user_exists = Users.objects.filter(User_Name=user, User_Password=pass1).exists()
        print(user_exists)
        if user_exists:
            url = reverse('lhome')
            getcode = Users.objects.filter(User_Name=user).first()
            User_Name = getcode.User_Name
            request.session['username'] = User_Name
            return HttpResponseRedirect(url)
        else:
            return render(request, "login.html")
    else:
        # Handle the GET request to render the login page
        return render(request, "login.html")
    
    


def signup(request):
    submitted = False

    if request.method == 'POST':
        form = Usersform(request.POST,request.FILES)
        if form.is_valid():
            username = form.cleaned_data['User_Name']
            if Users.objects.filter(User_Name=username).exists():
                # If username exists, add an error to the form
                form.add_error('User_Name', 'This username is already taken.')
            else:
                # If username is unique, save the form data
                form.save()
                submitted = True
                return render(request, "signup.html", {'form': form, 'submitted': submitted})
        
    else:
        form = Usersform()

    if 'submitted' in request.GET:
        submitted = True

    return render(request, "signup.html", {'form': form, 'submitted': submitted})

def blog(request):
    submitted = False
    blog_user = request.session.get('username')

    if request.method == 'POST':
        form = Blogform(request.POST, request.FILES)

        if form.is_valid():
            # Assign the blog_user value to Blog_User field after validation
            form.instance.Blog_User = blog_user
            form.save()
            submitted = True
            url = reverse('lhome')
            return HttpResponseRedirect(url)

        else:
            print(form.errors)  # Output form errors to console for debugging if needed

    else:
        form = Blogform()

    if 'submitted' in request.GET:
        submitted = True
    your_blog = Blogs.objects.filter(Blog_User=blog_user)
    return render(request, "Blog.html", {'form': form, 'submitted': submitted,'yours':your_blog})