from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def movieapi(request):
    try:
        if request.method=="GET":
            movies=Movie.objects.all()
            serializer=MovieSerializer(movies,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        if request.method=="POST":
            data=request.data
            serializer=MovieSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"success":"data entered"})
            else:
                return Response({"error":serializer.errors,"status":status.HTTP_400_BAD_REQUEST})
    except Exception as e:
        return Response({"error":"exception occurred"})
    
@api_view(['PUT','DELETE','GET',"PATCH"])
def movie_update(request,pk=None):
    try:
        if request.method=='PUT':
            instance=Movie.objects.get(pk=pk)
            serializer=MovieSerializer(instance,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data,"msg":"updated","status":status.HTTP_202_ACCEPTED})
            else:
                return Response({"error":serializer.errors})
            
        if request.method=='PATCH':
            instance=Movie.objects.get(pk=pk)
            serializer=MovieSerializer(instance,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data,"msg":"updated","status":status.HTTP_202_ACCEPTED})
            else:
                return Response({"error":serializer.errors})
        if request.method=="DELETE":
            try:
                obj=Movie.objects.get(id=pk)
                obj.delete()
                return Response({"success":"data deleted"})
            except Exception as e:
                return Response({"error":"data not found "})
            
        if request.method=="GET":
            try:
                obj=Movie.objects.get(id=pk)
                serializer=MovieSerializer(obj)
                return Response({"success":serializer.data})
            except Exception as e:
                return Response({"error":"data not found "})
    except Exception as e:
        print(e)
        return Response({"error":"exception occurred"})
            