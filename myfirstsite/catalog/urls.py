from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('task_detail/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task_list/', views.task_list, name='task_list'),
    path('review_detail/<int:review_id>/', views.review_detail, name='review_detail'),
    path('review_list/', views.review_list, name='review_list'),
    path('task_review_list/<int:task_id>/', views.task_review_list, name='task_review_list'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path("register_user/", views.register_user, name="register_user"),
    path("login_user/", views.login_user, name="login_user"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path('add_review/<int:task_id>/', views.add_review, name='add_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('upload/', views.image_upload_view),

]