import re

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer


@api_view(['GET', 'POST'])
def all_users(request):
    if request.method == 'GET':
        users = User.objects.all()

        return Response(
            UserSerializer(
                users,
                many=True).data
        )
    elif request.method == 'POST':
        # test entries
        username = request.data.get('username').strip()
        matchs = re.match("^[\\w.@+-]+$", username)
        if matchs is None:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=["username invalid"]
            )

        # creating new user
        try:
            user = User.objects.create_user(
                username=username,
                first_name=request.data.get('first_name'),
                last_name=request.data.get('last_name'),
                password=request.data.get('password'),
                is_active=request.data.get('is_active'),
            )
        except Exception as exp:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data=["something went wrong when saving user"]
            )

        return Response(UserSerializer(user).data)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def crud_users(request, id):
    if request.method == 'GET':
        user = User.objects.filter(id=id)

        return Response(
            UserSerializer(
                user[0]
            ).data if len(user) > 0 else []
        )
    elif request.method == 'PUT':
        print('\n\n')
        print('>>')
        user = User.objects.filter(id=id)
        if len(user) == 0:
            print('\n\n', len(user), len(user) == 0, '\n')
            Response([])
        else:
            print('-->', user)
            user = user[0]

        print('====')
        print('user.username', user.username)
        print('user.first_name', user.first_name)
        print('user.last_name', user.last_name)
        print('user.password', user.password)
        print('user.is_active', user.is_active)

        # user.username=request.username
        # user.first_name=request.first_name
        # user.last_name=request.last_name
        # user.password=request.password
        # user.is_active=request.password

        # print('+++')
        # try:
        #     user.save()
        # except:
        #     print('\n\n')
        #     Response('eu bosnia')

        # print('&&&&')
        # print('\n\n')
        return Response(UserSerializer(user).data)
    elif request.method == 'PATCH':
        pass
    elif request.method == 'DELETE':
        pass

    return Response('OK')
