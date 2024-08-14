

# Create your views here.
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from .models import *
from jobspireapp.models import *

from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm#to get inbuilt login formfrom shopingapp.models import *




# Create your views here.
def registerhirer(request):
    if request.method=='POST':
        form=HireRegistrationForm(request.POST)
        #request POST which is used to pass your POST data in to SellerRegistrationForm
        if form.is_valid():
            password=form.cleaned_data.get('password')
            cpassword=form.cleaned_data.get('cpassword')
            if password != cpassword:
                messages.error(request,"Password don't match")

            else:
                user=form.save(commit=False)
                user.set_password(password) #set password database save akiyal matre kodkn patu
                user.save()#commit=True
                messages.success(request,'Registration sucessfull.you can now login')
                return redirect(loginhirer)
    else:
        form=HireRegistrationForm() #storing our form

    return render(request,'hirerregister.html',{'form':form}) #form visible




def loginhirer(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                request.session['hireid'] =user.id
                #login() function used to login authenticated users

                messages.success(request,f'You are now logged in as{username}')
                return redirect('jobupload')
            else:
                messages.error(request,'Invalid username or password.')

        else:
            messages.error(request,'form is not valid')
    else:
        form=AuthenticationForm()
    return render(request,'hirerlogin.html',{'form':form})



def jobuploads(request):
    if request.method=='POST':
        jobtitle = request.POST.get('jobtitle')
        JobDescription=request.POST.get('description')
        location= request.POST.get('location')
        employmenttype= request.POST.get('employment-type')
        salary= request.POST.get('salary')
        contactemail=request.POST.get('contact-email')
        companyname=request.POST.get('companyname')
        companylogo=request.FILES.get('companylogo')
        category=request.POST.get('category')
        Requirements=request.POST.get('requirements')
        Schedule=request.POST.get('schedule')
        Additionalinformation=request.POST.get('additionalinformation')
        db=jobupload(jobtitle=jobtitle,JobDescription=JobDescription,location=location,
                     employmenttype=employmenttype,salary=salary,contactemail=contactemail,
                    companyname=companyname,companylogo=companylogo,
                     category=category,Requirements=Requirements,Schedule=Schedule,
                     Additionalinformation=Additionalinformation)
        db.save()
        return redirect(jobdis)

    return render(request,'jobupload.html')

def jobdis(request):
    id1 = request.session['hireid']
    data = User.objects.get(id=id1)
    category=request.GET.get('category','all') #get selected category ,if there is no category all option will work
    if(category=='all'):
        db=jobupload.objects.all() #fetch all products
    else:
        db=jobupload.objects.filter(category=category)

    return render(request,'jobdisplayadmin.html',{'data':data,'db':db})

def editproductdisplay(request, id):
        b = jobupload.objects.get(id=id)
        if (request.method == 'POST'):
            b.jobtitle = request.POST.get('jobtitle')
            b.JobDescription = request.POST.get('description')
            b.location = request.POST.get('location')
            b.employmenttype = request.POST.get('employment-type')
            b.salary = request.POST.get('salary')
            b.contactemail = request.POST.get('contact-email')
            b.companyname = request.POST.get('companyname')

            if (request.FILES.get('companylogo') == None):
                b.save()
            else:
                b.companylogo = request.FILES.get('companylogo')
            b.category = request.POST.get('category')
            b.Requirements = request.POST.get('requirements')
            b.Schedule = request.POST.get('schedule')
            b.Additionalinformation = request.POST.get('additionalinformation')
            b.save()
            return redirect(jobdis)
        return render(request, 'editjobs.html', {'data': b})


def delete(request,delid):
    db = jobupload.objects.get(id=delid)
    action = request.GET.get('action')
    if (action == 'delete'):
        db.delete()

    return redirect(jobdis)


