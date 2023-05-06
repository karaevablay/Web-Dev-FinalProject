from rest_framework import serializers

from api.models import *

class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    photo = serializers.URLField(read_only=True)
    title = serializers.CharField()
    brief_info = serializers.CharField()
    link = serializers.URLField(read_only=True)


class MemberSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    photo = serializers.URLField(read_only=True)
    brief_info = serializers.CharField()

    def create(self, data):
        member = Member.objects.create(first_name=data.get('first_name'),
                                        last_name=data.get('last_name'),
                                        photo=data.get('photo'),
                                        brief_info=data.get('brief_info'))

        return member


# for testing purposes
# class MemberSerializer2(serializers.ModelSerializer): #
#     class Meta:
#         model = Member
#         fields = ('id', 'first_name', 'last_name', 'photo', 'brief_info')


class MemberInfoSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = MemberInfo
        fields = ('id', 'member', 'email', 'about', 
        'education', 'skills', 'hobbies', 'github', 'tg')


class BlogSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = ('id', 'member', 'title', 'creation_date', 'content')
        