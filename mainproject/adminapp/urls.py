from django.urls import path
from .views import *
urlpatterns=[
    path('hireregister/',registerhirer),
    path('loginhirer/',loginhirer),
    path('jobupload/',jobuploads,name='jobupload'),
    path('jobdis/',jobdis),
    path('edit/<int:id>',editproductdisplay),
    path('delete/<int:delid>',delete)
]