from hubApp.models import Paper, Backend, Category

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


def test_Backend():
	t = Backend(name = 'Bob')
	assert str(t) == 'Bob'


def test_Category():
	t = Category(name = 'Bob', lookup_name = 'MLA')
	assert str(t) == 'Bob'


def test_Paper():
	t = Paper(title='Story of Bob', author='Bob', owner=User('Alice-Hamble'), 
		description='lorem ipsum', keywords='ML', link='github.test',
		backend = Backend.set('Jax'), votes=3, category='ML')
	assert str(t) == 'Story of Bob | Bob'
	assert get_absolute_url(t) == 'github.test'