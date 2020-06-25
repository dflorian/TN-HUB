from hubApp import models

def test_Backend():
	t = Backend('Bob')
	assert t.name == 'Bob'
