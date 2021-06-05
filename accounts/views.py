import os


from django.conf import settings
from django.contrib import auth, messages

from django.contrib.auth.models import User
from django.http import request, FileResponse, HttpResponse

from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.detail import BaseDetailView



from accounts.models import Files


def home(request):
    return render(request,'home.html')
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,'login.html')
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,"Username already exists")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"Email already exists")
            return redirect('register')
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save();
            messages.info(request,"User Created")
            return redirect('login')
    else:
        return render(request,'registration.html')


class TaskListView(ListView):
    model = Files
    template_name = 'dashboard.html'
    context_object_name = 'obj'

def logout(request):
    auth.logout(request)
    return redirect('/')

def upload(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        files=request.FILES['file']
        s = Files(title=title, pdf=files)
        s.save()
        return redirect('dashboard')
    else:
        return render(request,'upload.html')



class DisplayPdfView(BaseDetailView):
    def get(self, request, *args, **kwargs):
        objkey = self.kwargs.get('pk', None) #1
        pdf = get_object_or_404(Files, pk=objkey) #2
        fname = pdf.filename() #3
        path = os.path.join(settings.MEDIA_ROOT,fname)#4
        response = FileResponse(open(path, 'rb'), content_type="application/pdf")
        response["Content-Disposition"] = "filename={}".format(fname)
        return response