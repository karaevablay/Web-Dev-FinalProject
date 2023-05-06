from django.db import models

# Create your models here.


class Project(models.Model):
    photo = models.URLField()
    title = models.CharField(max_length=255)
    brief_info = models.CharField(max_length=255)
    link = models.URLField()

    def to_json(self):
        return {
            'id': self.id,
            'photo': self.photo,
            'title': self.title,
            'brief_info': self.brief_info,
            'link': self.link
        }
    

class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.URLField()
    brief_info = models.CharField(max_length=255)

    def to_json(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'photo': self.photo,
            'brief_info' : self.brief_info
        }


class MemberInfo(models.Model):
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    email = models.CharField(max_length=255)
    about = models.TextField()
    education = models.TextField()
    skills = models.TextField()
    hobbies = models.TextField()
    github = models.CharField(max_length=255)
    tg = models.CharField(max_length=255)


    def to_json(self):
        return {
            'id': self.id,
            'email': self.email,
            'about': self.about,
            'education': self.education,
            'skills': self.skills,
            'hobbies': self.hobbies,
            'github': self.github,
            'tg': self.tg
        }


class Blog(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    creation_date = models.DateTimeField()
    content = models.TextField()


    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'creation_date': self.creation_date,
            'content': self.content
        }