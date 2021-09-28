from django.urls import path
from .views import *


urlpatterns = [

    path('',HomeView.as_view(),name = 'home'),
    path('detail/<int:pk>',DetailView.as_view(),name = 'detail'),
    path('add_post/',AddPostView.as_view(),name = 'add_post'),
    path('detail/<int:pk>/comment/',AddCommentView.as_view(),name = 'add_comment'),
    path('like/',LikePost,name = 'like-post'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),

]