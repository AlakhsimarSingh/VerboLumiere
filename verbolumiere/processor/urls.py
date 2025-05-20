from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_view, name= 'login'),
    path('logout/', views.logout_view, name='logout'),
    path('',views.dashboard, name='dashboard'),
    path('upload/',views.upload_video, name='upload'),
    path('translate/<int:video_id>/', views.view_translation, name='translate'),
    path('delete/<int:video_id>/', views.delete_video, name='delete_video' ),
    path('register/',views.register_user, name='register_user')
]
