from django.http import Http404
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from auth_.models import MainUser
from auth_.serializers import MainUserWithProfileSerializer
from rest_framework import viewsets
from api.serializers import BlogSerializer, BlogDetailSerializer
from api.models import Blog


class UserWithProfileDetail(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, user_id):
        try:
            return MainUser.objects.get_all_users().get(pk=user_id)
        except MainUser.DoesNotExist:
            raise Http404

    def get(self, request, user_id, format=None):
        user_with_profile = self.get_object(user_id=user_id)
        serializer = MainUserWithProfileSerializer(user_with_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlogViewset(viewsets.GenericViewSet):
    def get_queryset(self):
        if self.action in ('update', 'delete'):
            return Blog.objects.filter(
                author_id=self.request.user,
                id=self.kwargs['blog_id']
            )

        if self.action == 'retrieve':
            try:
                return Blog.objects.select_related(
                    'author'
                ).get(pk=self.kwargs['blog_id'])
            except Blog.DoesNotExist:
                raise Http404

        if self.action == 'list':
            return Blog.objects.select_related(
                'author'
            ).filter(author_id=self.kwargs['author_id'])
        return Blog.objects.all()

    def get_serializer_class(self):
        if self.action in ('create', 'update'):
            return BlogSerializer
        if self.action in ('retrieve', 'list'):
            return BlogDetailSerializer

    def get_permissions(self):
        if self.action in ('create', 'update', 'delete'):
            self.permission_classes = (permissions.IsAuthenticated,)
        if self.action in ('retrieve', 'list',):
            self.permission_classes = (permissions.AllowAny,)
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        blog = self.get_queryset().first()
        serializer = self.get_serializer(blog, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        blog = self.get_queryset()
        blog.delete()
        return Response(status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        blog = self.get_queryset()
        serializer = self.get_serializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        blog_list = self.get_queryset()
        serializer = self.get_serializer(blog_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
