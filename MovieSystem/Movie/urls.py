from django.urls import path
from .views import CollectionDetailView, CollectionAPIView, get_request_count, reset_request_count, movie_api

urlpatterns = [
    path('movies/', movie_api),
    path('collection/', CollectionAPIView.as_view()),
    path('collection/<uuid:uuid>/', CollectionDetailView.as_view()),
    path('request-count/', get_request_count),
    path('request-count/reset/', reset_request_count)    
]
