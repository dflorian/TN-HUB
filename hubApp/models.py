from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Backend(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name


class Category(models.Model):
	name = models.CharField(max_length=255)
	lookup_name = models.CharField(max_length=255, default=name)

	def __str__(self):
		return self.name


class Paper(models.Model):
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	owner = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
	description = models.TextField()
	keywords = models.TextField()
	link = models.TextField()
	backend = models.ManyToManyField(Backend)
	votes = models.ManyToManyField(User, related_name='paper', default='0')
	publication_date = models.DateField(auto_now_add=True, editable=False)
	category = models.ManyToManyField(Category)


	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		#return reverse('paper-detail', args=(str(self.id)))
		return reverse('home')

	def get_backend(self):
		return ', '.join([a.name for a in self.backend.all()])

	def get_category(self):
		return ', '.join([a.name for a in self.category.all()])

	def total_votes(self):
		return self.votes.count()

	def voters(self):
		q = self.votes.values('username')
		if q:
			temp = [name['username'] for name in q]
			output = ", ".join(temp)
		else:
			output = 'no votes yet'	
		return output

	"""if q:
			temp = [name['username'] for name in q]
			output = temp[0]
			if len(temp) > 1:
				for val in range(1, len(temp)):
					output += ", " + str(temp[val])
			return output
		else:
			return "no votes"""