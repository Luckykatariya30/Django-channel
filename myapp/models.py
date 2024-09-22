from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=121)

    def __str__(self):
        return self.group_name

class Chat(models.Model):
    contant = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=True)
    group_name = models.ForeignKey('Group', on_delete=models.CASCADE)
    


