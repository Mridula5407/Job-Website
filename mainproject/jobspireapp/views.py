from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import render, HttpResponse, redirect
from django.utils.html import strip_tags

from .models import *
from django.template.loader import render_to_string
# Create your views here.

def userregister(request):
    if (request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        mobile = request.POST.get('mobile')
        workstatus = request.POST.get('workstatus')
        currentcity = request.POST.get('city')
        if password == cpassword:
            db = Registeration(fullname=name, email=email, password=password, mobile=mobile, workstatus=workstatus,
                               currentcity=currentcity)
            db.save()
            return redirect(userlogin)
        else:
            return HttpResponse('Registration failed')

    return render(request, 'user_register.html')


def userlogin(request):
    if (request.method == 'POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        dbase = Registeration.objects.all()
        for i in dbase:
            if (i.email == email and i.password == password):
                request.session['userid'] = i.id
                print(i.id)
                return redirect(personaldetailsupload)

        else:
            return HttpResponse('failed')
    return render(request, 'userlogin.html')


def firstprofileview(request):
    userid = request.session['userid']
    if request.method == 'POST':
        resume = request.FILES.get('r')
        resumeheadline = request.POST.get('resumehead')
        keyskills = request.POST.get('keyskills')
        projects = request.POST.get('projects')
        propic=request.FILES.get('propic')
        profilesummary=request.POST.get('profilesummary')

        try:
            register = Registeration.objects.get(id=userid)
            personaldetails = Personaldetails.objects.get(register=register)
            employmentdetails = employment.objects.get(register=register)
            educationdetails=educationmodel.objects.get(register=register)
            careerprofiles=carrerprofile.objects.get(register=register)
            print(personaldetails)
            print(employmentdetails)

            db = profile(
                register=register,
                personaldetails=personaldetails,
                employmentdetails=employmentdetails,
                educationdetails=educationdetails,
                carrerprofile=careerprofiles,
                resume=resume,
                resumeheadline=resumeheadline,
                keyskills=keyskills,
                projects=projects,
                profilepic=propic,
                profilesummary=profilesummary

            )
            db.save()
            return redirect(profile_display_all)

        except Registeration.DoesNotExist:
            return HttpResponse('Registeration not found', status=404)
        except Personaldetails.DoesNotExist:
            return HttpResponse('Personaldetails not found', status=404)
        except Exception as e:
            return HttpResponse(f'Error: {str(e)}', status=500)

    return render(request, 'firstprofile.html')


def personaldetailsupload(request):
    userid = request.session['userid']
    if request.method == 'POST':
        gender = request.POST.get('gender')
        martialstatus = request.POST.get('martial')
        dob = request.POST.get('dob')
        diffrentlyabled = request.POST.get('diffrentlyabled')
        careerbreak = request.POST.get('carrer')
        address = request.POST.get('Permanentaddress')
        hometown = request.POST.get('hometown')
        pincode = request.POST.get('pincode')
        register = Registeration.objects.get(id=userid)
        languages = request.POST.get('languages')
        dbase = Personaldetails(register=register, gender=gender, martialstatus=martialstatus, dob=dob,
                                diffrentlyabled=diffrentlyabled, careerbreak=careerbreak, address=address,
                                hometown=hometown, pincode=pincode, languages=languages)
        dbase.save()
        return redirect(employmentdetailsupload)
    return render(request, 'personal_detailsupload.html')


def employmentdetailsupload(request):
    userid = request.session['userid']
    if (request.method == 'POST'):
        currentemployment = request.POST.get('currentemployment')
        employmenttype = request.POST.get('Employmenttype')
        totalexperience = request.POST.get('years')
        currentcompanyname = request.POST.get('Currentcompanyname')
        jobtitle = request.POST.get('Currentjobtitle')
        joiningdate = request.POST.get('Joiningdate')
        currentsalary = request.POST.get('Currentsalary')
        skillsused = request.POST.get('Skillsused')
        jobprofile = request.POST.get('Jobprofile')
        noticeperiod = request.POST.get('Noticeperiod')
        register = Registeration.objects.get(id=userid)
        dbase = employment(register=register, currentemployment=currentemployment, employmenttype=employmenttype,
                           totalexperience=totalexperience, currentcompanyname=currentcompanyname, jobtitle=jobtitle,
                           joiningdate=joiningdate, currentsalary=currentsalary, skillsused=skillsused,
                           jobprofile=jobprofile, noticeperiod=noticeperiod)
        dbase.save()
        return redirect(educationaldetailsupload)
    return render(request, 'employmentdetailsupload.html')



def educationaldetailsupload(request):
    userid = request.session['userid']
    if (request.method == 'POST'):
        education = request.POST.get('Education')
        university=request.POST.get('University')
        course=request.POST.get('Course')
        specialization=request.POST.get('Specialization')
        coursetype=request.POST.get('Coursetype')
        coursedurationstart=request.POST.get('coursedurationstart')
        coursedurationend = request.POST.get('coursedurationend')
        gradingsystem=request.POST.get('gradingsystem')
        register = Registeration.objects.get(id=userid)
        db=educationmodel(register=register,education=education,university=university,course=course,specialization=specialization,coursetype=coursetype,coursedurationstart=coursedurationstart,coursedurationend=coursedurationend,gradingsystem=gradingsystem)
        db.save()
        return redirect(careerprofileupload)
    return render(request, 'educationdetailsupload.html')


def careerprofileupload(request):
    userid = request.session['userid']
    if (request.method == 'POST'):
        currentindustry=request.POST.get('Current')
        department=request.POST.get('department')
        rolecategory=request.POST.get('role')
        desiredjobtype=request.POST.get('jobtype')
        employmenttype=request.POST.get('emptype')
        shift=request.POST.get('shift')
        location=request.POST.get('location')
        salary=request.POST.get('salary')
        register =Registeration.objects.get(id=userid)
        dbase=carrerprofile(register=register,currentindustry=currentindustry,department=department,
                            rolecategory=rolecategory,jobtype=desiredjobtype,employmenttype=employmenttype,
                            shift=shift,location=location,expectedsalary=salary)
        dbase.save()
        return  redirect(firstprofileview)
    return render(request,'carrerprofileupload.html')


def index(request):
    return render(request,'index.html')


def carrer(request):
    return render(request,'careers.html')
def contact(request):
    return render(request,'contact.html')
def companies(request):
    return render(request,'company.html')


def profile_display_all(request):
    userid = request.session['userid']
    data = Registeration.objects.get(id=userid)
    profiles =profile.objects.get(register=data)
    return render(request, 'profiledisplay.html', {'data':data,'p':profiles})

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
        return HttpResponse ("sucessfully")

    return render(request,'jobupload.html')

def updatereg(request):
    id1 = request.session['userid']
    d=Registeration.objects.get(id=id1)
    if(request.method=='POST'):
        d.fullname=request.POST.get('fullname')
        d.email = request.POST.get('email')
        d.mobile= request.POST.get('mobile')
        d.workstatus = request.POST.get('workstatus')
        d.currentcity = request.POST.get('city')
        print(d)
        d.save()

        return redirect(profile_display_all)

    return render(request, 'updatereg.html', {'data':d})



def updatepersonaldetails(request):
    id1 = request.session['userid']
    d=Personaldetails.objects.get(id=id1)
    if(request.method=='POST'):
        d.gender = request.POST.get('gender')
        d.martialstatus = request.POST.get('martial')
        d.dob = request.POST.get('dob')
        d.diffrentlyabled = request.POST.get('diffrentlyabled')
        d.careerbreak = request.POST.get('carrer')
        d.address = request.POST.get('Permanentaddress')
        d.hometown = request.POST.get('hometown')
        d.pincode = request.POST.get('pincode')
        d.languages = request.POST.get('languages')
        print(d)
        d.save()

        return redirect(profile_display_all)

    return render(request, 'updatepersonaldetails.html', {'data':d})


def updateemployment(request):
    id1 = request.session['userid']
    d = employment.objects.get(id=id1)
    if (request.method == 'POST'):
        d.currentemployment = request.POST.get('currentemployment')
        d.employmenttype = request.POST.get('Employmenttype')
        d.totalexperience = request.POST.get('years')
        d.currentcompanyname = request.POST.get('Currentcompanyname')
        d.jobtitle = request.POST.get('Currentjobtitle')
        d.joiningdate = request.POST.get('Joiningdate')
        d.currentsalary = request.POST.get('Currentsalary')
        d.skillsused = request.POST.get('Skillsused')
        d.jobprofile = request.POST.get('Jobprofile')
        d.noticeperiod = request.POST.get('Noticeperiod')
        d.save()
        return redirect(profile_display_all)

    return render(request, 'updatemployment.html', {'data': d})


def updatecarrer(request):
    userid = request.session['userid']
    d=carrerprofile.objects.get(id=userid)
    if (request.method == 'POST'):
        d.currentindustry=request.POST.get('Current')
        d.department=request.POST.get('department')
        d.rolecategory=request.POST.get('role')
        d.desiredjobtype=request.POST.get('jobtype')
        d.employmenttype=request.POST.get('emptype')
        d.shift=request.POST.get('shift')
        d.location=request.POST.get('location')
        d.expectedsalary=request.POST.get('salary')
        d.save()
        return redirect(profile_display_all)

    return render(request, 'updatecarrer.html', {'data': d})

def updateeducational(request):
    userid = request.session['userid']
    d=educationmodel.objects.get(id=userid)
    if (request.method == 'POST'):
        d.education = request.POST.get('Education')
        d.university=request.POST.get('University')
        d.course=request.POST.get('Course')
        d.specialization=request.POST.get('Specialization')
        d.coursetype=request.POST.get('Coursetype')
        d.coursedurationstart=request.POST.get('coursedurationstart')
        d.coursedurationend=request.POST.get('coursedurationend')
        d.gradingsystem=request.POST.get('gradingsystem')
        d.save()
        return redirect(profile_display_all)

    return render(request, 'updateeducation.html', {'data': d})


def updatepicresume(request):
    userid = request.session['userid']
    d=profile.objects.get(id=userid)
    if(request.method=='POST'):
        if(request.FILES.get('propic')==None):
            d.save()
        else:
            d.profilepic=request.FILES.get('propic')
        d.save()
        return redirect(profile_display_all)

    return render(request, 'updatepicresume.html', {'data': d})

def updateresume(request):
    userid =request.session['userid']
    d=profile.objects.get(id=userid)
    if (request.method == 'POST'):
        if (request.FILES.get('resume') == None):
            d.save()
        else:
            d.resume = request.FILES.get('resume')

        d.save()
        return redirect(profile_display_all)
    return render(request, 'updateresume.html', {'data': d})



def updateresumeheadline(request):
    userid = request.session['userid']
    d = profile.objects.get(id=userid)
    if (request.method == 'POST'):
        d.resumeheadline = request.POST.get('resumehead')
        d.save()
        return redirect(profile_display_all)
    return render(request, 'updateresumeheadline.html', {'data': d})





def updateprojectsprofilesummary(request):
    userid=request.session['userid']
    d =profile.objects.get(id=userid)
    if (request.method == 'POST'):
        d.projects = request.POST.get('projects')
        d.profilesummary = request.POST.get('profilesummary')
        d.save()
        return redirect(profile_display_all)
    return render(request, 'updateprojectsprofilesummary.html', {'data': d})

def updatekeyskills(request):
    userid = request.session['userid']
    d = profile.objects.get(id=userid)
    if (request.method == 'POST'):
        d.keyskills = request.POST.get('keyskills')
        d.save()
        return redirect(profile_display_all)
    return render(request, 'updatekeyskills.html', {'data': d})


def jobviews(request):
    id1 = request.session['userid']
    data = Registeration.objects.get(id=id1)
    category=request.GET.get('category','all') #get selected category ,if there is no category all option will work
    if(category=='all'):
        db=jobupload.objects.all() #fetch all products
    else:
        db=jobupload.objects.filter(category=category)

    return render(request,'jobdisplay.html',{'data':data,'db':db})

def singleview(request,id):
    db=jobupload.objects.get(id=id)
    return render(request,'singlejobdisplay.html',{'data':db})





def addtomyjob(request,itemid):
    item=jobupload.objects.get(id=itemid)
    apply=applyitem.objects.all()

    for i in apply:
        if(i.item.id==itemid and i.userid==request.session['userid']):
            i.save()

            return redirect(myjobdisplay)
    else:
            db=applyitem(userid=request.session['userid'],item=item)
            db.save()
            return redirect(myjobdisplay)


def myjobdisplay(request):
    id1=request.session['userid']
    db = applyitem.objects.filter(userid=id1)

    return render(request,'myjobdisplay.html',{'data':db})


def deletemyjob(request,deleteids):
    db = applyitem.objects.get(id=deleteids)
    action = request.GET.get('action')
    if (action == 'delete'):
        db.delete()

    return redirect(myjobdisplay)



def savedjobs(request,saveid):
    item=jobupload.objects.get(id=saveid)
    save=savejob.objects.all()

    for i in save:
        if(i.saved.id==saveid and i.userid==request.session['userid']):
            i.save()
            return redirect(savedjobdisplay)
    else:
            db=savejob(userid=request.session['userid'],saved=item)
            db.save()
            return redirect(savedjobdisplay)


def savedjobdisplay(request):
    id1=request.session['userid']
    db = savejob.objects.filter(userid=id1)

    return render(request,'savedjobdisplay.html',{'data':db})

def deletesavejob(request,deleteid):
    db = savejob.objects.get(id=deleteid)
    action = request.GET.get('action')
    if (action == 'delete'):
        db.delete()

    return redirect(savedjobdisplay)


# views.py
from django.core.mail import send_mail

from django.shortcuts import render, get_object_or_404
from .models import JobApplication, jobupload


def job_application_view(request,id):
    if request.method == 'POST':
        userid = request.session.get('userid')
        name = request.POST.get('name')
        email = request.POST.get('email')
        cover_letter = request.POST.get('cover_letter')
        resume = request.FILES.get('resume')
        user = Registeration.objects.get(id=userid)

        # Get the job instance (assuming job ID is passed in POST data)
        # job_id = request.POST.get('job_id')  # or however you are passing the job ID
        job = get_object_or_404(jobupload,id=id)

        application = JobApplication(job=job, user=user, name=name, email=email, cover_letter=cover_letter,
                                     resume=resume)
        application.save()

        return redirect(job_application_display)
    else:
        # Handle GET request or other cases
        return render(request, 'job_application.html')








  # Ensure 'userlogin' is the name of your login URL or view
def job_application_display(request):
    data =JobApplication.objects.order_by('-id').first()
    userid = request.session.get('userid')

    if not userid:
        # Handle case where userid is not in session, e.g., redirect to login
        return redirect('userlogin')


    return render(request, 'jobapplicationdisplay.html', {'data': data})


def createapplication(request):  # after payment
    if request.method == 'POST':
        apply_items = []
        userid = request.session.get('userid')  # userid session calling

        if not userid:
            # Handle case where user is not logged in
            return redirect(userlogin)

        # Retrieve user and address details
        user = Registeration.objects.get(id=userid)  # registered details
        jobs = applyitem.objects.filter(userid=userid)  # cart filter

        # Create the order object
        applies = Applies.objects.create(
            userdetails=user)  # (create): automatically save avum .save nn pakaram use cheyunnu. this method is used to create a new instance of a model and save it to the database.

        # Process each item in cart
        for i in jobs:  # cart iteration
            Appliedjob.objects.create(
                apply=applies,
                jobpic=i.item.companylogo,
                companyname=i.item.companyname,
                jobtitle=i.item.jobtitle,
            )

            apply_items.append({'companyname': i.item.companyname, 'jobtitle': i.item.jobtitle})

        # Construct email content
        subject = 'Jobspire Apply'
        context = {'apply_items': apply_items}  # list of items
        html_message = render_to_string('jobuploadconfirmationmail.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'mridulamanikandan2003@gmail.com'
        to_mail = [user.email]

        # Send mail
        send_mail(subject, plain_message, from_email, to_mail, html_message=html_message,)
        jobs.delete()

        return redirect(submitsucessfull)

    return HttpResponse('Invalid request method')


from django.shortcuts import render, redirect
from .models import applyitem

def summary(request):
    userid = request.session.get('userid')

    if not userid:
        # Handle case where user is not logged in
        return redirect(userlogin)

    apply_items = applyitem.objects.filter(userid=userid)
    return render(request, 'summary.html', {'a': apply_items})




def Applyview(request):
    userid=request.session['userid']
    a=Appliedjob.objects.filter(apply__userdetails__id=userid).order_by('-apply__Applieddate')
    print(a)
    return render(request,'allapply.html', {'apply':a})

def submitsucessfull(request):
    return render(request,'submitted.html')



