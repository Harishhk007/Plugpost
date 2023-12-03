from django.db import models

class Users(models.Model):
    
    User_Name=models.CharField(max_length=100,null=False,blank=False)
    User_Password=models.CharField(max_length=100,null=False,blank=False)
    User_Fullname=models.CharField(max_length=100,null=False,blank=False)
    User_Id=models.AutoField(primary_key=True,auto_created=True)
    User_Age=models.IntegerField(max_length=100,null=False,blank=False)
    User_Img=models.ImageField(null=True,blank=True,upload_to="images/")
    User_Gender=models.CharField(max_length=100,null=False,blank=False)
    User_Phone=models.IntegerField(max_length=100,null=False,blank=False)
    User_Email=models.EmailField(max_length=100,null=False,blank=False)
    User_Dob=models.DateField(max_length=100,null=False,blank=False)
    

    def __str__(self):
        return self.User_Name

class Blogs(models.Model):
    Title=models.CharField(max_length=1000,null=False,blank=False)
    Desc=models.CharField(max_length=1000,null=False,blank=False)
    category=models.CharField(max_length=100,null=False,blank=False)
    Cover_img=models.ImageField(null=True,blank=True,upload_to="images/")
    Article=models.CharField(max_length=30000,null=False,blank=False)
    related_img=models.ImageField(null=True,blank=True,upload_to="images/")
    Blog_User=models.CharField(max_length=100,default="Unknown")

    def __str__(self):
        return f"{self.Title} - {self.Blog_User}"


