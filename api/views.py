from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly



@csrf_exempt
@api_view(['GET', 'POST'])
def movie_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getMovie(request, pk):
    """
    Retrieve, update or delete a movie instance.
    """
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(movie, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def timetracker_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        movies = TimeTracker.objects.all()
        serializer = TimeTrackerSerializer(movies, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = TimeTrackerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'PUT', 'DELETE'])
def task_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        movies = Tasks.objects.all()
        serializer = taskSerializer(movies, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = taskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def time_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        movies = Time.objects.all()
        serializer = timeSerializer(movies, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = timeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def date_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        movies = Date.objects.all()
        serializer = dateSerializer(movies, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = dateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def event_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        movies = Events.objects.all()
        serializer = eventsSerializer(movies, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = eventsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        movies = User_Log.objects.all()
        serializer = userSerializer(movies, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Create your views here.
