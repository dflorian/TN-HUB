from hubApp import models

class BackendTest(TestCase):
	
	def test_Backend():
		t = Backend('Bob')
		assert t.name == 'Bob'
