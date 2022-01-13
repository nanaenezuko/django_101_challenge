from django.urls import path
from .views import HomePageView, PhotoPostDetailView, PostPhotoView

app_name = 'photouploader'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('detail/<int:pk>/', PhotoPostDetailView.as_view(), name='detail'),
    path('post/', PostPhotoView.as_view(), name='post'),
]
