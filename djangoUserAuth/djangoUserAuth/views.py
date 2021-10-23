from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model


@api_view(['GET'])
def all_users(request):
    userModel = get_user_model()
    users = userModel.objects.all()
    print('users', users)

    return users
