from .models import Paper, Backend

class BackendTest():
	
	def test_Backend():
		t = Backend('Bob')
		assert t.name == 'Bob'
