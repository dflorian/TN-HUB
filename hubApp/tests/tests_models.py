from hubApp import models

class BackendTest():
	
	def test_Backend():
		t = Backend('Bob')
		assert t.name == 'Bob'
