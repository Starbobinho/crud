from rest_framework import status
from rest_framework.views import APIView, Response
from .models import User
from .serializers import UserSerializer

class CrudAPI(APIView):
    def get(self, request):
        users = User.objects.all()
        users_data = UserSerializer(users, many=True).data
        response_data = {"datas": users_data}
        return Response(response_data, status=status.HTTP_200_OK)
    
    def post(self,request):
        atributos = [request.data.get('name'), request.data.get('last_name'), request.data.get('cpf'), request.data.get('email'), request.data.get('is_active')]
        User.objects.create(name=atributos[0], last_name=atributos[1], cpf=atributos[2], email=atributos[3], is_active=True)
        response_data = {"response": "User created"}
        return Response(response_data, status=status.HTTP_200_OK)

    def put(self, request, id):
        user = User.objects.filter(id=id).first()
        name = request.data.get('name')
        if user is None:
            response_data = {"response": "Item doesnot exists"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        user.name = name
        user.save()
        response_data = {"response": "item Updated"}
        return Response(response_data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        user = User.objects.filter(id=id).first()
        if user is None:
            response_data = {"response": "User doesnot exists"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        user.is_active = False
        user.save()
        response_data = {"response": "User Deleted"}
        return Response(response_data, status=status.HTTP_200_OK)