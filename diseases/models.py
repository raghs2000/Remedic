from django.db import models

# Create your models here.
class Disease(models.Model):
	
	name = models.CharField(max_length=50, unique=True)
	congenial = models.CharField(max_length=50)
	age_group = models.CharField(max_length=50)
	classification = models.CharField(max_length=50)
	causes = models.CharField(max_length=50)
	prevention = models.CharField(max_length=50)
	treatment = models.CharField(max_length=50)

	# add region, cases, symptoms
	
	def __str__(self):
		return self.name