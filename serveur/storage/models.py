from django.db import models
from django.utils import timezone

  
class Photo(models.Model):
    name= models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photos/")
    date = models.DateTimeField(default=timezone.now, verbose_name="Date ajout")

    class Meta:
        ordering = ['date']

    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.name