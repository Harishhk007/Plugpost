from django.shortcuts import render
from .models import Users
from .models import Blogs
from .forms import Usersform
from django.db.models import Q
from .forms import Blogform
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request,"home.html")
def lhome(request):
    your_blog = Blogs.objects.all().order_by('-Blog_id')
    user=Users.objects.all()
    return render(request,"LHOME.html",{'yours':your_blog,'users':user})
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
    user=Users.objects.all()
    return render(request, "Blog.html", {'form': form, 'submitted': submitted,'yours':your_blog,'users':user})

def read(request,Blog_id):
    read = get_object_or_404(Blogs, Blog_id=Blog_id)
    name=read.Blog_User
    print(name)
    user = get_object_or_404(Users, User_Name=name)
    user1=Users.objects.all()
    return render(request,"read.html",{"read":read,"user":user,'users':user1})

def searchoption(request,blogcat):
    blogcat1=Blogs.objects.filter(category=blogcat).order_by('-Blog_id')
    blogcatname=blogcat
    user=Users.objects.all()
    return render(request,"search-option.html",{'blog':blogcat1,'blogcatname':blogcatname,'users':user})

def search_blog(request):
    if request.method == 'POST':
        query=request.POST.get('searchbar')
        print(query)  # Get the search query from the request
        if query:
            # Split the query into individual words
            search_words = query.split()
            search_words1 = query.split()

            # Initialize an empty Q object to construct the query dynamically
            q_object = Q()
            q_object1 = Q()

            # Construct OR condition for each word in the search query
            for word in search_words:
                q_object |=Q(Title__icontains=word) | Q(Blog_User__icontains=word)
            for word1 in search_words1:
                q_object1 |= Q(User_Name__icontains=word1)

            # Perform a query to find titles containing any of the specified words
            blog_posts = Blogs.objects.filter(q_object)
            users=Users.objects.filter(q_object1)
        else:
            blog_posts = Blogs.objects.none() 
        user1=Users.objects.all() # Return an empty queryset if no query is provided

        return render(request, 'searchblog.html',{'blog_post':blog_posts,'user':users,'users':user1})
    
def aboutus(request):
    user=Users.objects.all()
    return render(request,"aboutus.html",{'users':user})
def userprofile(request, User_Name):
    user1 = Users.objects.filter(User_Name=User_Name)
    blogs = Blogs.objects.filter(Blog_User=User_Name)  # Assuming Blog_User is related to Users model

    return render(request, "userprofile.html", {"user": user1, 'blogs': blogs})
def contact(request):
    user=Users.objects.all()
    return render(request,"contact.html",{'users':user})