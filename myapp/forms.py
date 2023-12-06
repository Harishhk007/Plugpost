from django import forms
from .models import Users
from .models import Blogs
# Define the choices outside the form class
GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

CATEGORY=[
    ('Technology','Technology'),
    ('Sports','Sports'),
    ('Programming','Programming'),
    ('Design','Design'),
    ('Social','Social'),
    ('Others','Others'),
]

class Usersform(forms.ModelForm):
    # Define the form fields here
    
    User_Name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'style':'border:3px solid white;width:300px;background-color:transparent;font-size:20px;border-radius:20px;outline:0;color:white;font-family:"poppins";','placeholder':'Enter Username'}))
    User_Password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':'border:3px solid white;width:300px;background-color:transparent;font-size:20px;border-radius:20px;outline:0;color:white;font-family:"poppins";', 'placeholder':'Enter Password'}))
    User_Fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'style':'border:3px solid white;width:300px;background-color:transparent;font-size:20px;border-radius:20px;outline:0;color:white;font-family:"poppins";', 'placeholder':'Enter Full name'}))
    User_Age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','style':'border:3px solid white;width:300px;background-color:transparent;font-size:20px;border-radius:20px;outline:0;color:white;font-family:"poppins";', 'placeholder':'Enter Age'}))
    User_Img = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control','style':'border:3px solid white;width:300px;background-color:transparent;font-size:20px;border-radius:20px;outline:0;color:white;font-family:"poppins";'}))
    User_Gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control','style':'border:3px solid white;width:300px;height:100%;background-color:transparent;font-size:20px;border-radius:20px;outline:0;color:white;font-family:"poppins";',}))
    User_Phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','style':'border:3px solid white;width:300px;background-color:transparent;font-size:20px;border-radius:20px;outline:0;color:white;font-family:"poppins";', 'placeholder':'Enter phone Number'}))
    User_Email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','style':'border:3px solid white;width:300px;background-color:transparent;font-size:20px;border-radius:20px;outline:0;color:white;font-family:"poppins";', 'placeholder':'Enter Email'}))
    User_Dob = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'style':'border:3px solid white;width:300px;background-color:transparent;font-size:20px;border-radius:20px;outline:0;color:white;font-family:"poppins";','placeholder':'Enter DOB'}))

    class Meta:
        model = Users
        fields = ('User_Name', 'User_Password', 'User_Fullname', 'User_Age', 'User_Img', 'User_Gender', 'User_Phone', 'User_Email', 'User_Dob')
        labels = {
            'User_Name': 'Username',
            'User_Password': 'Password',
            'User_Fullname': 'Fullname',
            'User_Age': 'Age',
            'User_Img': 'Profile Photo',
            'User_Gender': 'Gender',
            'User_Phone': 'Phone Number',
            'User_Email': 'Email',
            'User_Dob': 'Date of Birth',
        }


class Blogform(forms.ModelForm):
    Title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'style':'border:3px solid white;width:500px;background-color:transparent;font-size:20px;border-radius:5px;outline:0;color:white;font-family:"poppins";','placeholder':'Enter Title'}))
    Desc = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':'border:3px solid white;width:500px;background-color:transparent;font-size:20px;border-radius:5px;outline:0;color:white;font-family:"poppins";', 'placeholder':'Enter Description'}))
    category = forms.ChoiceField(choices=CATEGORY, widget=forms.Select(attrs={'class': 'form-control','style':'text-align:center;border:3px solid white;margin:40px;width:500px;height:100%;background-color:transparent;font-size:20px;border-radius:5px;outline:0;color:white;font-family:"poppins";',}))
    Cover_img = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control','style':'padding-bottom:15px;border:3px solid white;width:500px;background-color:transparent;font-size:20px;border-radius:5px;outline:0;color:white;font-family:"poppins";'}))
    Article = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'10','cols':'60', 'style':'border:3px solid white;width:500px;background-color:transparent;font-size:20px;border-radius:5px;outline:0;color:white;font-family:"poppins";', 'placeholder':'Enter Your Article'}))
    
    
    related_img = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control','style':'padding-bottom:15px;border:3px solid white;width:500px;background-color:transparent;font-size:20px;border-radius:5px;outline:0;color:white;font-family:"poppins";'}))
    Blog_User = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'style':'border:3px solid white;width:500px;background-color:transparent;font-size:20px;border-radius:5px;outline:0;color:white;font-family:"poppins";','placeholder':'Enter Title'}),required=False)
    class Meta:
        model = Blogs
        fields = ('Title', 'Desc', 'category', 'Cover_img', 'Article', 'related_img','Blog_User')
        