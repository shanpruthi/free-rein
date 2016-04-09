from django.db import models

# Create your models here.

class Products(models.Model):
	title = models.CharField(max_length = 200)
	description = models.TextField(max_length = 400)
	image = models.ImageField(upload_to='static/tinycarousel/images')
	price = models.IntegerField()
	tags = models.CharField(max_length=100, blank=True)


	def __unicode__(self):
		return title

	class Meta:
		verbose_name_plural = "Products"
