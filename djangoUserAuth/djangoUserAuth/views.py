from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer


@api_view(['GET', 'POST'])
def all_users(request):
    if request.method == 'GET':
        users = User.objects.all()

        # usernames = [UserSerializer(user) for user in users]

        return Response(
            UserSerializer(
                users,
                many=True).data
        )
    elif request.method == 'POST':
        return Response(
            {'Leoanrdo Da Vinci says:': 'did I understand it wrong or I was suppose to write in a object within a post method call? .-. Are you sure? ^^"'}
        )
