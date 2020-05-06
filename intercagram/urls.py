"""intercagram URL Configuration """


from django.contrib import admin
from django.urls import path
from intercagram import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hello-world/', views.hello_world),
    #path('server-time/', views.server_time),
    path('hi/', views.hi),
]
