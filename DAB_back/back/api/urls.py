from django.urls import path
from api.views  import *

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('projects/', projects_list),
    path('members/', members_list),
    path('members/<int:pk>/', MemberInfoAPIView.as_view()),
    path('blogs/', BlogsView.as_view()),
    path('blogs/<int:pk>/', BlogInfoView.as_view())
]