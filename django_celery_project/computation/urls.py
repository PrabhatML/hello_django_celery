from django.urls import path
from computation.views import GenerateRandomUserView,UserListView

urlpatterns = [
    path("celery_generate_user/",GenerateRandomUserView.as_view(),name="generate_list"),
    path("users_list/",UserListView.as_view(),name="users_list"),
]