import os
import requests
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from dotenv import load_dotenv
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Collection
from .serializers import CollectionSerializer
from django.http import JsonResponse

load_dotenv()

@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes((IsAuthenticated, ))
def movie_api(request):
    response = requests.get(
        os.environ.get("MOVIE_API_URL"),
        auth=(os.environ.get("CLIENT_ID"), os.environ.get("CLIENT_SECRET"))
        )
    status = dict(response.json()).get("is_success", True)

    # Retry Mechanism
    while status == False:
        response = requests.get(
        os.environ.get("MOVIE_API_URL"),
        auth=(os.environ.get("CLIENT_ID"), os.environ.get("CLIENT_SECRET"))
        )
        status = dict(response.json()).get("is_success", True)
    return JsonResponse(response.json(), safe=False)

class CollectionAPIView(generics.ListCreateAPIView):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()

    def get_queryset(self):
        return Collection.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CollectionSerializer(queryset, many=True)

        collections_data = []
        genres_set = dict()

        for data in serializer.data:
            print(data)
            collections_data.append({
                "title": data["title"],
                "uuid": data["uuid"],
                "description": data["description"],
            })

            movies = data["movies"]
            print(movies)
            for movie in movies:
                genres = movie.get("genres", "").split(",") if "genres" in movie else []
                for genre in genres:
                    genres_set[genre] = genres_set.get(genre, 0) + 1

        # Get top 3 favorite genres based on the count
        top_genres = dict(sorted(genres_set.items(), key=lambda x: x[1], reverse=True)[:3])
        favorite_genres = ", ".join(top_genres.keys())


        response_data = {
            "is_success": True,
            "data": {
                "collections": collections_data,
                "favourite_genres": favorite_genres,
            }
        }

        return Response(response_data)
    
    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        collection_serializer = self.get_serializer(data=request.data)
        if collection_serializer.is_valid(raise_exception=True):
            uuid=collection_serializer.save()

        response_data = {
            "collection_uuid": str(uuid.pk)
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

class CollectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    lookup_field = "uuid"

    def retrieve(self, request, *args, **kwargs):
        res = super().retrieve(request, *args, **kwargs)
        res.data.pop("uuid")
        res.data.pop("user")
        return Response(data=res.data, status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        res = super().update(request, *args, **kwargs)
        res.data.pop("uuid")
        res.data.pop("user")
        return Response(data=res.data, status=status.HTTP_200_OK)

# For request counts
@api_view(['GET'])
def get_request_count(request):
    count_middleware = getattr(request, 'count_middleware', None)
    count = count_middleware.get_request_count()
    return Response({"requests": count})

@api_view(['POST'])
def reset_request_count(request):
    if request.method == 'POST':
        count_middleware = getattr(request, 'count_middleware', None)
        count_middleware.reset_request_count()
        return Response({'message': 'Request count reset successfully'})
