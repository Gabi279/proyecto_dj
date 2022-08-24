from django.db import models

class ProjectsManager(models.Manager):
    
    def last_projects(self, name):
        return self.filter('__all__')