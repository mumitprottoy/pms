from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self) -> str:
        return self.name


class Node(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self) -> str:
        return self.name
    

class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    volume = models.IntegerField(default=0)
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    

class ProjectMember(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='members')
    member = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='projects')
    assigned_node = models.ForeignKey(Node, on_delete=models.CASCADE)


class Sector(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='sectors')
    node = models.ForeignKey(
        Node, on_delete=models.CASCADE, related_name='projects')
    head = models.OneToOneField(ProjectMember, on_delete=models.CASCADE)


class KPI(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    percentage = models.IntegerField(default=0)
    

class ProjectProgress(models.Model):
    sector = models.OneToOneField(
        Sector, on_delete=models.CASCADE, related_name='progress')
    percentage = models.IntegerField(default=0)
    is_delivered = models.BooleanField(default=False)
