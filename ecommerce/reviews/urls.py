from django.urls import include, path
from . import views 
from .views import reviews 

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('<int:review_id>/', views.review_detail, name='review_detail'),
]
