from django.urls import path
from . import views

#The namespace is defined by the application using the app_name variable.
app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
]