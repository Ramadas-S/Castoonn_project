from django.urls import re_path,path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    ###################################################################################<<<<<<<<< LANDING MODULE >>>>>>>>>>>>>>>>>
    path('', views.index, name='index'),
    path('user_type', views.user_type, name='user_type'),
    path('login_main',views.login_main, name='login_main'),

    ################################################################################### <<<<<<<<< CREATOR MODULE >>>>>>>>>>>>>>>>>
    path('creator_registration/',views.creator_registration,name='creator_registration'),
    path('index_creator_confirmation/<int:user_id>/',views.index_creator_confirmation,name='index_creator_confirmation'),
    path('artist_registration/',views.artist_registration,name='artist_registration'),
    path('index_artist_confirmation/<int:user_id>/',views.index_artist_confirmation,name='index_artist_confirmation'),

    ################################################################################### <<<<<<<<< Artist MODULE >>>>>>>>>>>>>>>>>
    


    
    ]