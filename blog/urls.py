from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='posts'),
    path('about/', views.about, name='about'),
    path('post/create', views.create_post, name='post-create'),
    path('contact/', views.contact, name='contact'),
    path('post/edit/<int:id>/', views.edit_post, name='post-edit'),
    path('post-delete<int:id>/', views.delete_post, name='post-delete')
]


