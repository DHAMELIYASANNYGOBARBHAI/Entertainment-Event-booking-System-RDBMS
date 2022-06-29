"""Event_Registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('showcust', views.showcust, name = "showcust"),
    path('insert', views.InsertCust, name="InsertTmp"),
    path('Edit/<int:c_id>', views.EditCust, name="EditCust"),
    path('Update/<int:c_id>', views.UpdateCust, name="UpdateCust"),
    path('Delete/<int:c_id>', views.DeleteCust, name="DeleteCust"),
    path('runQueryCustomer',views.runQueryCustomer,name="runQueryCustomer"),

    path('',views.homepage,name="homepage"),
    
    path('showevent', views.showevent, name = "showevent"),
    path('insertevent', views.Insertevent, name="Insertevent"),
    path('Editevent/<int:event_id>', views.EditEvent, name="EditEvent"),
    path('Updateevent/<int:event_id>', views.UpdateEvent, name="UpdateEvent"),
    path('Deleteevent/<int:event_id>', views.DeleteEvent, name="DeleteEvent"),
    path('runQueryEvent',views.runQueryEvent,name="runQueryEvent"),
]
