
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AnimalSerializer

from .models import Animal

class AnimalView(APIView):
   
    def get(self,request):
        animals = Animal.objects.all()
        animals_json = AnimalSerializer(animals,many=True)
        return Response(animals_json.data,status.HTTP_200_OK)
    
    def post(self,request):
        try:

            serializer = AnimalSerializer(data=request.data)
            serializer.is_valid() 
            serializer.save()

            return Response(serializer.data,status.HTTP_201_CREATED)
        except KeyError:
            an_dict = {**request.data}
            animal = AnimalSerializer(data=an_dict)
            animal.is_valid()
            
            return Response(animal.errors,status.HTTP_400_BAD_REQUEST)

class AnimalIdView(APIView):
    
    def patch(self,request,id):
        # tratar também no método update
        try:
            if request.data.get('sex'):
                return Response({"sex": "You can not update sex property."},status.HTTP_422_UNPROCESSABLE_ENTITY)
            elif request.data.get('group') and request.data.get('traits'):
                return Response({"group": "You can not update group property.","traits": "You can not update traits property."},status.HTTP_422_UNPROCESSABLE_ENTITY)
            elif request.data.get('group'):
                return Response({"group": "You can not update group property."},status.HTTP_422_UNPROCESSABLE_ENTITY)
            elif request.data.get('traits'):
                return Response({"traits": "You can not update traits property."},status.HTTP_422_UNPROCESSABLE_ENTITY)
            animal = Animal.objects.get(id=id)
            
            serializer = AnimalSerializer(animal,request.data,partial=True)
            serializer.is_valid()
            serializer.save()

            return Response(serializer.data,status.HTTP_200_OK)
        except:
            return Response({"detail":"Not found."},status.HTTP_404_NOT_FOUND)
    def get(self,request,id):
        try:
            animal = Animal.objects.get(id=id)
            serializer = AnimalSerializer(animal)

            return Response(serializer.data,status.HTTP_200_OK)
        except:
            return Response({"detail":"Not found."},status.HTTP_404_NOT_FOUND)

    def delete(self,request,id):
        try:
            animal = Animal.objects.get(id=id)
            animal.delete()


            return Response({},status.HTTP_200_OK)
        except:
            return Response({"detail":"Not found."},status.HTTP_404_NOT_FOUND)
