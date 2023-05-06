import json
from django.http.response import JsonResponse

from api.models import *
from api.serializers import *

from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import Http404
from rest_framework.permissions import IsAuthenticated

# for fbv:
from rest_framework.decorators import api_view, permission_classes

# for cbv:
from rest_framework.views import APIView

@api_view(["GET"])
def projects_list(request):
    if request.method == "GET":
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


@api_view(["GET", "POST"])
def members_list(request):
    if request.method == "GET":
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



class MemberInfoAPIView(APIView):

    def get_object(self, pk):
        try:
            return MemberInfo.objects.get(id=pk)
        except Exception:
            return Response({'message': 'an error occurred'});

    def get(self, request, pk=None):
        memberInfo = self.get_object(pk)
        serializer = MemberInfoSerializer(memberInfo)
        return Response(serializer.data)



class BlogsView(APIView):
     def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class BlogInfoView(APIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Blog.objects.get(id=pk)
        except Blog.DoesNotExist as e:
            raise Http404
    
    def get(self, request, pk=None):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, pk=None):
        blog = self.get_object(pk)
        serializer = BlogSerializer(instance=blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        blog = self.get_object(pk)
        blog.delete()
        return Response({'message': 'deleted vacancy'}, status=204)
