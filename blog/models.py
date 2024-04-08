from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    titutlo = models.CharField(max_length=120)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'posts'
        
    def __str__(self):
        return self.titutlo

