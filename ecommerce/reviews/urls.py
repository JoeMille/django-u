from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('', views.review_list, name='review_list'),
    path('<int:review_id>/', views.review_detail, name='review_detail'),
]