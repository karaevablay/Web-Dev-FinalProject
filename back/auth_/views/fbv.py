from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from auth_.models import MainUser
from auth_.serializers import MainUserBriefSerializer


@api_view(['GET', ])
@permission_classes((AllowAny,))
def user_list(request):
    if request.method == 'GET':
        users = MainUser.objects.get_user_data_for_home_page()
        serializer = MainUserBriefSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
