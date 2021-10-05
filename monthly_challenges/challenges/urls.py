from django.urls import path
from .import views

urlpatterns = [
    #path("january", views.january),
    #path("february", views.february)
    #path("<month>",views.monthly_challenges)
    #path("<int:month>",views.monthly_challenges_by_number),
    #path("<str:month>",views.monthly_challenges),
    #path("",views.index),
    path("",views.index_by_template),
    path("<int:month>",views.monthly_challenges_redirect_by_number),
    #path("<str:month>",views.monthly_challenges_by_dict,name="month-challenge")
    path("<str:month>",views.monthly_challenges_by_template,name="month-challenge")
]
