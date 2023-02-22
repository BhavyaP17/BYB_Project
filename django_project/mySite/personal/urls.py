"""
1. In the configuration directory urls.py file we have referenced another urls.py in
webapp/. However, if you have a look at the files inside your webapp directory, you
will see that a urls.py file doesn't exist there. This means that we have to create a
new Python file called urls.py inside your webapp/ directory. Once you have
created the new urls.py file, copy and paste the following code into it:

The above code in webapp/ urls.py references a function called index from
views.py. This function doesn't exist yet, so let's open webapp/views.py and define
this function.

"""

from django.urls import path, include
from . import views

app_name='personal'
urlpatterns = [
    path('', views.index, name='index'),
    path('CV', views.CV, name='CV'),
    path('Contact', views.Contact, name='Contact'),
    path('OnlineShoppingWebsite',views.OnlineShoppingWebsite, name='OnlineShoppingWebsite'),    
]
