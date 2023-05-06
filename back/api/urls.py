from django.urls import path
from api.views.fbv import project_list
from auth_.views.fbv import user_list
from api.views.cbv import BlogViewset, UserWithProfileDetail

urlpatterns = [
    path('projects/', project_list, name='project list'),
    path('users/', user_list, name='user list'),
    path('users/<int:user_id>/', UserWithProfileDetail.as_view()),
    path('users/<int:author_id>/blog/', view=BlogViewset.as_view(
        {
            'post': 'create',
            'get': 'list'
        }
    ), name='create or list blog'),
    path('users/<int:author_id>/blog/<int:blog_id>/', view=BlogViewset.as_view(
        {
            'delete': 'delete',
            'put': 'update',
            'get': 'retrieve'
        }
    ),
         name='retrieve, delete or update blog'
         ),
]
