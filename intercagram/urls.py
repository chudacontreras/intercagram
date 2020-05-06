"""intercagram URL Configuration """


from django.contrib import admin
from django.urls import path
from intercagram import views as local_views
from posts import views as posts_views


urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('hello-world/', views.hello_world),
    #path('server-time/', views.server_time),
    #path('hi/', views.hi),
    path('hello-world/', local_views.hello_world),
    path('sorted/', local_views.sort_integers),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),

    path('posts/', posts_views.list_posts),
    
]
