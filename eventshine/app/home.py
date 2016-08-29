from .models import User

u = User(name='Test User', password='testPassword')
u.save()

# userID = models.CharField(max_length=200)
# name = models.CharField(max_length=200)
# paymentName = models.CharField(max_length=200)
# paymentNumber = models.CharField(max_length=200)
# password = models.CharField(max_length=100)
