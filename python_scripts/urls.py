from django.urls import path
from . import views


urlpatterns = [
    #(ano makikita sa url, ung function na tinatawag from views, tawag mo sa path na to)
    path ('',views.home,name='home'), #or the index.html, then define in views.py
    # path ('',views.welcome,name='welcome')

    # path for add when they request for the add url
    path ('compute',views.compute,name='compute'),
    
    # path for add when they request for the add url ChooseFile1/
    path ('ChooseFile1',views.ChooseFile1,name='ChooseFile1'),
    
    # path for add when they request for the add url ChooseFile2/
    path ('ChooseFile2',views.ChooseFile2,name='ChooseFile2'),


]



