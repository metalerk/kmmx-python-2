from __future__ import unicode_literals

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from uuid import uuid4

NATIONALITIES = (
	('US', 'UNITED STATES'),
	('MX', 'MEXICO'),
	('ES', 'SPAIN'),
	('UK', 'UNITED KINGDOM'),
	('AR', 'ARGENTINA'),
)

class Author(models.Model):
	id = models.UUIDField(primary_key=True,
						  default=uuid4,
						  editable=False)
	nickname = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)
	age = models.PositiveIntegerField(default=18,
									  validators=[
									  	MaxValueValidator(100),
									  	MinValueValidator(18)])
	nationality = models.CharField(max_length=50,
								   choices=NATIONALITIES,
								   default='MX')

	def __unicode__(self):
		return self.nickname

class Post(models.Model):
	id = models.UUIDField(primary_key=True,
						  default=uuid4,
						  editable=False)
	title = models.CharField(max_length=150)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True,
									  auto_now=False)
	updated_at = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.title
