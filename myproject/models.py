from django.db import models
import datetime
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    pr_id=models.IntegerField()
    pr_name=models.CharField(max_length=100)
    pr_image=models.ImageField(upload_to='pic')
    pr_description=models.TextField()
    pr_quanity=models.IntegerField(null=False,blank=False)
    trending=models.BooleanField(default=False, help_text="0-default, 1-Trending")


    @property
    def prdoucturl(self):
            try:
                url=self.imageurl
            except:
                url=""
            return url
    def __str__ (self):
        return self.pr_name
class compare(models.Model):
     Name=models.CharField(max_length=100)
     image=models.ImageField(upload_to='pic')
     


     @property
     def compareurl(self):
        try:
            url=self.imageurl
        except:
             url=""
        return url
     def __str__ (self):
        return self.Name
     
class Iphone(models.Model):
     Name=models.CharField(max_length=100)
     i_image=models.ImageField(upload_to='pic')
     price=models.CharField(max_length=20)
     pr_quanity=models.IntegerField(null=False,blank=False)
     trending=models.BooleanField(default=False, help_text="0-default, 1-Trending")





     @property
     def Iphoneurl(self):
        try:
            url=self.i_image.url
        except:
             url=""
        return url
     def __str__ (self):
        return self.Name
     
class Iphonepro(models.Model):
     I_image=models.ImageField(upload_to='pic')
     
     @property
     def Iphoneprourl(self):
        try:
            url=self.I_image.url
        except:
             url=""
        return url
     def __str__ (self):
        return self.I_image

class phonepro(models.Model):
    Description=models.CharField(max_length=20)
    name=models.CharField(max_length=200)
    InTheBox=models.CharField(max_length=100)
    I_name=models.CharField(max_length=100)
    Warranty=models.CharField(max_length=50)
    W_name=models.CharField(max_length=100)



    def __str__ (self):
        return self.name

    
class  Features(models.Model):
    a_name=models.TextField(max_length=1000)
    b_name=models.TextField(max_length=1000)
    c_name=models.TextField(max_length=1000)
    d_name=models.TextField(max_length=1000)
    e_name=models.TextField(max_length=1000)
    f_name=models.TextField(max_length=1000)
    g_name=models.TextField(max_length=1000)
    h_name=models.TextField(max_length=1000)
    k_name=models.TextField(max_length=1000)


    def __str__ (self):
        return self.a_name
   
                   # iphone16

class myphone(models.Model):
     Name=models.CharField(max_length=100)
     my_image=models.ImageField(upload_to='pic')
     price=models.CharField(max_length=20)
     pr_quanity=models.IntegerField(null=False,blank=False)
     trending=models.BooleanField(default=False, help_text="0-default, 1-Trending")



     def __str__ (self):
        return self.Name
     @property
     def myphoneurl(self):
        try:
            url=self.my_image.url
        except:
             url=""
        return url

     def __str__ (self):
        return self.Name

class my(models.Model):
     p_image=models.ImageField(upload_to='pic')
    


     @property
     def myurl(self):
        try:
            url=self.p_image.url
        except:
             url=""
        return url    


class pro(models.Model):
    Description=models.CharField(max_length=20)
    name=models.CharField(max_length=200)
    InTheBox=models.CharField(max_length=100)
    I_name=models.CharField(max_length=100)
    Warranty=models.CharField(max_length=50)
    W_name=models.CharField(max_length=100)



class  ok(models.Model):
    a_name=models.TextField(max_length=1000)
    b_name=models.TextField(max_length=1000)
    c_name=models.TextField(max_length=1000)
    d_name=models.TextField(max_length=1000)
    e_name=models.TextField(max_length=1000)
    f_name=models.TextField(max_length=1000)
    g_name=models.TextField(max_length=1000)
    h_name=models.TextField(max_length=1000)
    k_name=models.TextField(max_length=1000)


                    # iphone15.html

class mm(models.Model):
     Name=models.CharField(max_length=100)
     my_image=models.ImageField(upload_to='pic')
     price=models.CharField(max_length=20)
     pr_quanity=models.IntegerField(null=False,blank=False)
     trending=models.BooleanField(default=False, help_text="0-default, 1-Trending")

    



     @property
     def mmurl(self):
        try:
            url=self.my_image.url
        except:
             url=""
        return url
     
class sari(models.Model):
     p_image=models.ImageField(upload_to='pic')
    


     @property
     def sariurl(self):
        try:
            url=self.p_image.url
        except:
             url=""
        return url    
     

class aaa(models.Model):
    Description=models.CharField(max_length=20)
    name=models.CharField(max_length=200)
    InTheBox=models.CharField(max_length=100)
    I_name=models.CharField(max_length=100)
    Warranty=models.CharField(max_length=50)
    W_name=models.CharField(max_length=100)



class  bbb(models.Model):
    a_name=models.TextField(max_length=1000)
    b_name=models.TextField(max_length=1000)
    c_name=models.TextField(max_length=1000)
    d_name=models.TextField(max_length=1000)
    e_name=models.TextField(max_length=1000)
    f_name=models.TextField(max_length=1000)
    g_name=models.TextField(max_length=1000)
    h_name=models.TextField(max_length=1000)
    k_name=models.TextField(max_length=1000)


                # iphone14.html

class ts(models.Model):
     Name=models.CharField(max_length=100)
     my_image=models.ImageField(upload_to='pic')
     price=models.CharField(max_length=20)
     pr_quanity=models.IntegerField(null=False,blank=False)
     trending=models.BooleanField(default=False, help_text="0-default, 1-Trending")





     @property
     def tsurl(self):
        try:
            url=self.my_image.url
        except:
             url=""
        return url
     
class eee(models.Model):
     p_image=models.ImageField(upload_to='pic')
    


     @property
     def eeeurl(self):
        try:
            url=self.p_image.url
        except:
             url=""
        return url    

class ddd(models.Model):
    Description=models.CharField(max_length=20)
    name=models.CharField(max_length=200)
    InTheBox=models.CharField(max_length=100)
    I_name=models.CharField(max_length=100)
    Warranty=models.CharField(max_length=50)
    W_name=models.CharField(max_length=100)


class  ggg(models.Model):
    a_name=models.TextField(max_length=1000)
    b_name=models.TextField(max_length=1000)
    c_name=models.TextField(max_length=1000)
    d_name=models.TextField(max_length=1000)
    e_name=models.TextField(max_length=1000)
    f_name=models.TextField(max_length=1000)
    g_name=models.TextField(max_length=1000)
    h_name=models.TextField(max_length=1000)
    k_name=models.TextField(max_length=1000)


class Cart(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)


class iphoneplus(models.Model):
     Name=models.CharField(max_length=100)
     my_image=models.ImageField(upload_to='pic')
     price=models.CharField(max_length=20)
     pr_quanity=models.IntegerField(null=False,blank=False)
     trending=models.BooleanField(default=False, help_text="0-default, 1-Trending")





     @property
     def iphoneplusurl(self):
        try:
            url=self.my_image.url
        except:
             url=""
        return url
     
class plus(models.Model):
     p_image=models.ImageField(upload_to='pic')
    


     @property
     def eeeurl(self):
        try:
            url=self.p_image.url
        except:
             url=""
        return url    

class iplus(models.Model):
    Description=models.CharField(max_length=20)
    name=models.CharField(max_length=200)
    InTheBox=models.CharField(max_length=100)
    I_name=models.CharField(max_length=100)
    Warranty=models.CharField(max_length=50)
    W_name=models.CharField(max_length=100)


class  plus16(models.Model):
    a_name=models.TextField(max_length=1000)
    b_name=models.TextField(max_length=1000)
    c_name=models.TextField(max_length=1000)
    d_name=models.TextField(max_length=1000)
    e_name=models.TextField(max_length=1000)
    f_name=models.TextField(max_length=1000)
    g_name=models.TextField(max_length=1000)
    h_name=models.TextField(max_length=1000)
    k_name=models.TextField(max_length=1000)




