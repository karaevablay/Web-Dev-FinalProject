from django.http import Http404
from rest_framework import generics, mixins, permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from auth_.models import MainUser, Profile
from auth_.serializers import MainUserSerializer, ProfileSerializer
from auth_.serializers import MainUserWithProfileSerializer


class MainUsersListApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = MainUser.objects.all()
    serializer_class = MainUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProfileApiView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
