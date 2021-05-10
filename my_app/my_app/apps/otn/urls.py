from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('otn_letter_tube', views.otn_letter_tube, name='otn_letter_tube'),
    path('otn_letter_apparatus', views.otn_letter_apparatus, name='otn_letter_apparatus'),

]
