from django.urls import path

from accounts import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('upload',views.upload, name ='upload'),
    path('dashboard',views.TaskListView.as_view(),name='dashboard'),
    path('docview/<int:pk>',views.DisplayPdfView.as_view(),name='docview'),

]