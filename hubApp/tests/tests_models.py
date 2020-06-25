from .hubApp.models import *

def test_Backend():
	t = Backend('Bob')
	assert t.name == 'Bob'
