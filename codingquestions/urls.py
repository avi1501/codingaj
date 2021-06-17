from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home.as_view(), name="homepage"),
    # path("content/", views.content.as_view(), name="content"),
    path("blog/", views.blog.as_view(), name="blog"),
    path("<slug:slug>/", views.content1.as_view(), name="datatype"),
    path("content/<slug:slug>/", views.contentquestion.as_view(), name="question"),
    path("questions", views.all_questions.as_view(), name="all_questions"),
    path("questions/<slug:slug>", views.tagQuestionView.as_view(), name="tagView"),
    path("blog/<slug:slug>", views.blogView.as_view(), name="blogView"),
    

    

]
