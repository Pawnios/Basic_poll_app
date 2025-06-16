from django.db import models

from django.utils import timezone
import datetime
# Create your models here.

class question_cls(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days=1))
	
	
    
class choice_cls(models.Model):
	question=models.ForeignKey(question_cls,on_delete=models.CASCADE)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text
	
  