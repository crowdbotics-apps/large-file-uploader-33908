from django.urls import path
from home import views

urlpatterns = [
    path('', views.UploadView.as_view(), name='upload'),
    path('signed-up/', views.SignedURLView.as_view(), name='signed-up')
]
