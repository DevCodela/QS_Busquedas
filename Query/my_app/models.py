from django.db import models

class Libro(models.Model):
	autor = models.CharField(max_length=40)
	editor = models.CharField(max_length=30, blank=True, null=True)
	fecha_publicacion = models.DateField()
	

	def __unicode__(self):
		return self.autor
