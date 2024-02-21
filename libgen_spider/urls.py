from django.urls import path
from . import views

urlpatterns = [
    path('', views.scrape_website, name='scrape_website'),  # URL for the list of blogs
    # path('<int:blog_id>/', views.blog_detail, name='blog_detail'),  # URL for individual blog detail
    # path('filter/<str:title>/', views.blog_filter, name='blog_filter'),  # URL for filtering blogs by title
    # path('<int:blog_id>/comment/', views.add_comment, name='add_comment'),  # URL for adding comments
]
