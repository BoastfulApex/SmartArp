from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=200, null=True, blank=True)
    manager = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.project_name
    

class Sotsial(models.Model):
    sotsial_name = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.sotsial_name


class PostType(models.Model):
    post_type = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.post_type

   
class ContentPlan(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    post_type = models.ForeignKey(PostType, on_delete=models.CASCADE)
    sotsial = models.ForeignKey(Sotsial, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=False)
    history = models.BooleanField(default=False)
    
   
class PostCheck(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    post_type = models.ForeignKey(PostType, on_delete=models.CASCADE)
    sotsial = models.ForeignKey(Sotsial, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=False)
    history = models.BooleanField(default=False)
    
