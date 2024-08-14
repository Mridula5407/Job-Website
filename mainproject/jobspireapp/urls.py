from django.urls import path
from .views import *
urlpatterns=[

    path('userregister/',userregister),
    path('userlogin/',userlogin),
    path('firstprofile/',firstprofileview),
    path('personaldetailsupload/',personaldetailsupload),
    path('employmentdetailsupload/',employmentdetailsupload),
    path('educationaldetailsupload/',educationaldetailsupload),
    path('carrerupload/',careerprofileupload),
    path('profiledisplayall/',profile_display_all),
    path('index/',index),
    path('updatereg/',updatereg),
    path('updatepersonal/',updatepersonaldetails),
    path('updateemployment/',updateemployment),
    path('updatecarrer/',updatecarrer),
    path('updateeducation/',updateeducational),
    path('updatepic/',updatepicresume),
    path('updateresume/',updateresume),
    path('updateproject/',updateprojectsprofilesummary),
    path('updatekeyskill/',updatekeyskills),
    path('updateresumeheadline/',updateresumeheadline),
    path('jobupload/',jobuploads),
    path('jobdisplay/',jobviews),
    path('savejob/<int:saveid>',savedjobs),
    path('savedjobdisplay/',savedjobdisplay),
    path('deletesavejob/<int:deleteid>',deletesavejob),
    path('apply/<int:id>',job_application_view),
    path('createapply/',createapplication),
    path('summary/',summary),
    path('applyview/',Applyview),
    path('jobapplicationdisplay/',job_application_display),
    path('addtomyjob/<int:itemid>',addtomyjob),
    path('myjobdisplay/',myjobdisplay),
    path('deletemyjob/<int:deleteids>',deletemyjob),
    path('singlejobdisplay/<int:id>',singleview),
    path('carrers/',carrer),
    path('contact/',contact),
    path('company/',companies),
    path('submit/',submitsucessfull)
    # path('application_success/',application_success_view)



]