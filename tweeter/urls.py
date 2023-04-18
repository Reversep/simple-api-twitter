from django.urls import path

from . import views

urlpatterns = [
    path('tweet/', views.TweetListCreateAPIView.as_view() ),
    path('comment/', views.CommentListCreateApiView.as_view() ),
    path('mark/', views.MarkListCreateApiView.as_view() ),
]