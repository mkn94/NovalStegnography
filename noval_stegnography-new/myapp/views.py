from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import UserAccount
from .form import UserAccountForm,HiddenImageForm
from django.contrib.auth import logout
from .DB import DbConnection
from django.views.generic import View

dbobj=DbConnection(host="localhost",user="root",passwd="",database="noval_stegnography",port=3306)
def signup(request):
    return render(request,'signup.html')

def signupaction(request):
    username=request.POST['txtusername']
    password=request.POST['txtpassword']
    firstname=request.POST['txtfirstname']
    lastname=request.POST['txtlastname']
    address=request.POST['txtaddress']
    mobile=request.POST['txtmobile']
    email2=request.POST['txtemail']
    status=0
    role='user'
    useraccount=UserAccount.objects.create(username=username,password=password,role=role,firstname=firstname,lastname=lastname,address=address,mobile=mobile,email=email2,status=status)
    try:
        useraccount.save()
        return redirect(login)
    except:
        errmsg='User Registration Failed'
        return render(request,'signup.html',{'errmsg':errmsg})
    
def home(request):
    role=request.session['role']
    if role=='admin':
        return render(request,'adminhome.html')
    else:
        return render(request,'userhome.html')
    

def home1(request):
    return render(request,'home.html')
    
def login(request):
    form=UserAccountForm()
    return render(request,'login1.html',{'form':form})

def loginaction(request):
    username=request.POST["username"]
    password=request.POST["password"]
    record=UserAccount.objects.filter(username=username,password=password,status=1)
    if record.count()>0:
        record=UserAccount.objects.get(username=username,password=password)
        request.session['username'] = record.username
        request.session['role']=record.role
        if record.role=="admin":
            return render(request,'adminhome.html')
        else:
            return render(request,'userhome.html')
    else:
        form=UserAccountForm()
        return render(request,'login1.html',{'errmsg':'Invlid username or password, or your account is not activated','form':form})

def editlogin(request,id):
    login = UserAccount.objects.get(userid=id)
    return render(request,'editlogin.html', {'login':login})

def updatelogin(request, id):
    login = UserAccount.objects.get(userid=id)
    form = UserAccountForm(request.POST, instance = login)
    if form.is_valid():
        form.save()
        return render(request,'editusers.html')
    else:
        login = UserAccount.objects.get(userid=id)
        return render(request,'editlogin.html', {'login':login})

def deletelogin(request, id):
    login = UserAccount.objects.get(userid=id)
    login.delete()
    logins=UserAccount.objects.all()
    return render(request,'adminhome.html',{'logins':logins})

def editprofile(request):
    username=request.session['username']
    login = UserAccount.objects.get(username=username)
    return render(request,'editprofile.html', {'login':login})

def updateprofile(request):
    username=request.session['username']
    firstname=request.POST['txtfirstname']
    lastname=request.POST['txtlastname']
    address=request.POST['txtaddress']
    mobile=request.POST['txtmobile']
    email=request.POST['txtemail']
    sql="update useraccount set firstname=%s, lastname=%s, address=%s, email=%s, mobile=%s where username=%s"
    val=(firstname,lastname,address,email,mobile,username,)
    try:
        dbobj.executenonquery(sql,val)
        return redirect(home)
    except:
        errmsg='Update Failed'
        username=request.session['username']
        login = UserAccount.objects.get(username=username)
        return render(request,'editprofile.html', {'login':login,'errmsg':errmsg})
        
def custom_logout(request):
    logout(request)
    return redirect('login')

def changepassword(request):
    return render(request,'changepassword.html')

def updatepassword(request):
    password=request.POST['password']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    username=request.session['username']
    sql="select password from useraccount where username=%s"
    val=(username,)
    p=getstring(sql,val)
    if p==password:
        if newpassword==confirmpassword:
            sql="update useraccount set password=%s where username=%s"
            val=(newpassword,username)
            if dbobj.executenonquery(sql,val):
                errmsg='Password changed successfully'
                return render(request,'changepassword.html',{'errmsg':errmsg})
            else:
                errmsg='Unable to change password at this time'
                return render(request,'changepassword.html',{'errmsg':errmsg})
        else:
            errmsg='New Password and Confirm Password must be the same'
            return render(request,'changepassword.html',{'errmsg':errmsg})
    else:
        errmsg='Invalid Current Password'
        return render(request,'changepassword.html',{'errmsg':errmsg})
    

def getstring(sql,val):
    d=dbobj.selectrecords(sql,val)
    print(sql)
    s=""
    for row in d:
        s=row[0]
    print("password:"+str(s))
    return s

def validateuser(request):
    logins=UserAccount.objects.filter(status=0)
    return render(request,'validateuser.html',{'logins':logins})

def approveuser(request,username):
    sql="update useraccount set status=1 where username=%s"
    print(username)
    val=(username,)
    dbobj.executenonquery(sql,val)
    return redirect (validateuser)
    

def rejectuser(request,username):
    sql="delete from useraccount where username=%s"
    val=(username,)
    dbobj.executenonquery(sql,val)
    return redirect (validateuser)

def editusers(request):
    logins=UserAccount.objects.all()
    return render(request,'editusers.html',{'logins':logins})


from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import cv2
import hashlib


from django.shortcuts import render
from .form import HiddenImageForm
from .models import HiddenImage
from django.views import View
from stegano import lsb
from django.db.models import F
import os
from django.conf import settings
from cryptography.fernet import Fernet


def aaa(request):
    return render(request,'encrypted_image.html')

class HideMessageView(View):
    def get(self, request):
        form = HiddenImageForm()
        return render(request, 'hide.html', {'form': form})

    def post(self, request):
        form = HiddenImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES.get('image')
            hidden_text = request.POST.get('text')

            # Generate a random AES key
            key = Fernet.generate_key()
            cipher_suite = Fernet(key)

            # Encrypt the hidden text with the AES key
            encrypted_text = cipher_suite.encrypt(hidden_text.encode())

            hidden_image = HiddenImage(image=image_file, encrypted_text=encrypted_text)
            hidden_image.save()

            # Save the AES key to the database
            hidden_image.aes_key = key
            hidden_image.save()

            return render(request, 'success.html')
        else:
            return render(request, 'hide.html', {'form': form})

def decrypt(request):
    if request.method == 'POST' and 'image' in request.FILES:
        uploaded_file = request.FILES['image']

        try:
            # Retrieve the corresponding AES key from the database
            hidden_image = HiddenImage.objects.get(image=uploaded_file)
            key = hidden_image.aes_key
            cipher_suite = Fernet(key)

            # Decrypt the hidden text with the AES key
            decrypted_text = cipher_suite.decrypt(hidden_image.encrypted_text).decode()

            return render(request, "decrypt.html", {'decrypt': decrypted_text})
        except Exception as e:
            return render(request, "decrypt.html", {'error_message': str(e)})
    else:
        return render(request, "decrypt.html")
