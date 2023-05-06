from rest_framework import serializers
from auth_.serializers import MainUserShortSerializer
from api.models import Project
from api.models import Blog


class ProjectSerializer(serializers.ModelSerializer):
    author = MainUserShortSerializer()

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'photo', 'url', 'author')


class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(
        read_only=True
    )
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    location = serializers.CharField()
    title = serializers.CharField()
    text = serializers.CharField()

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.location = validated_data.get('location', instance.location)
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance


class BlogDetailSerializer(serializers.ModelSerializer):
    author = MainUserShortSerializer()

    class Meta:
        model = Blog
        fields = ('id', 'author', 'date_of_creation', 'date_of_updating', 'location', 'title', 'text')
