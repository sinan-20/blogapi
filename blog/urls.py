from django.urls import path
from blog import views



urlpatterns=[

    path("users/",views.CreateUserView.as_view()),
    path("posts/",views.PostListCreateView.as_view()),
    path("posts/<int:pk>/",views.PostReterieveUpdateDestroyView.as_view()),

    path("posts/<int:pk>/comments/",views.CommentCreateView.as_view())


    
]