
from django.db import models

# Create your models here.

class Registeration(models.Model):
    fullname = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    mobile = models.IntegerField(null=True)
    workstatus = models.CharField(max_length=100,null=True)
    currentcity = models.CharField(max_length=100,null=True)

class Personaldetails(models.Model):
    register= models.ForeignKey(Registeration, on_delete=models.CASCADE)
    gender = models.CharField(max_length=30)
    martialstatus = models.CharField(max_length=100)
    dob = models.DateField()
    diffrentlyabled = models.CharField(max_length=30)
    careerbreak = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    hometown = models.CharField(max_length=100)
    pincode = models.IntegerField()
    languages = models.CharField(max_length=100)

class employment(models.Model):
    register= models.ForeignKey(Registeration, on_delete=models.CASCADE)
    currentemployment = models.CharField(max_length=100)
    employmenttype = models.CharField(max_length=100)
    totalexperience = models.CharField(max_length=100)
    currentcompanyname = models.CharField(max_length=100)
    jobtitle = models.CharField(max_length=100)
    joiningdate = models.DateField()
    currentsalary = models.IntegerField()
    skillsused = models.CharField(max_length=100)
    jobprofile = models.CharField(max_length=100)
    noticeperiod = models.CharField(max_length=100)


class educationmodel(models.Model):
    register = models.ForeignKey(Registeration, on_delete=models.CASCADE)
    education=models.CharField(max_length=100)
    university=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)
    coursetype=models.CharField(max_length=100)
    coursedurationstart=models.CharField(max_length=100)
    coursedurationend=models.CharField(max_length=100)
    gradingsystem=models.CharField(max_length=100)


class carrerprofile(models.Model):
    register=models.ForeignKey(Registeration, on_delete=models.CASCADE)
    currentindustry=models.CharField(max_length=500)
    department=models.CharField(max_length=500)
    rolecategory=models.CharField(max_length=100)
    jobtype=models.CharField(max_length=100)
    employmenttype=models.CharField(max_length=100)
    shift=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    expectedsalary=models.IntegerField()



class profile(models.Model):
    register= models.ForeignKey(Registeration, on_delete=models.CASCADE)
    personaldetails = models.OneToOneField(Personaldetails, on_delete=models.CASCADE, null=True, blank=True)
    employmentdetails = models.ForeignKey(employment, on_delete=models.CASCADE,null=True, blank=True)
    educationdetails=models.ForeignKey(educationmodel,on_delete=models.CASCADE,null=True, blank=True)
    carrerprofile=models.ForeignKey(carrerprofile,on_delete=models.CASCADE,null=True, blank=True)
    resume = models.FileField(upload_to='pdf/')
    resumeheadline = models.CharField(max_length=200)
    keyskills = models.CharField(max_length=200)
    projects = models.CharField(max_length=100)
    profilesummary=models.CharField(max_length=100,null=True)
    profilepic=models.ImageField(upload_to='images/',null=True,blank=True,)






class jobupload(models.Model):
    jobtitle=models.CharField(max_length=100)
    JobDescription=models.CharField(max_length=500)
    Requirements=models.CharField(max_length=500)
    Additionalinformation=models.CharField(max_length=500)
    Schedule=models.CharField(max_length=500)
    location=models.CharField(max_length=100)
    employmenttype=models.CharField(max_length=100)
    salary=models.CharField(max_length=100)
    contactemail=models.CharField(max_length=200)
    companyname=models.CharField(max_length=200)
    companylogo=models.ImageField(upload_to='image/')
    category=models.CharField(max_length=100)

class applyitem(models.Model):
    userid=models.IntegerField()
    item=models.ForeignKey(jobupload,on_delete=models.CASCADE)


class savejob(models.Model):
    userid=models.IntegerField()
    saved=models.ForeignKey(jobupload,on_delete=models.CASCADE)


# models.py
from django.db import models

class JobApplication(models.Model):
    job = models.ForeignKey(jobupload, on_delete=models.CASCADE)
    user = models.ForeignKey(Registeration, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.CharField(max_length=500)

    def _str_(self):
        return self.name

class Applies(models.Model):
    userdetails=models.ForeignKey(Registeration,on_delete=models.CASCADE)
    Applieddate=models.DateTimeField(auto_now_add=True)


class Appliedjob(models.Model):
    apply=models.ForeignKey(Applies,on_delete=models.CASCADE)
    jobpic=models.ImageField()
    companyname=models.CharField(max_length=200)
    jobtitle= models.CharField(max_length=200)
    jobstatus=models.CharField(max_length=100)






