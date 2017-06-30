from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MessageManager(models.Manager):
	def add_message(self, sender, content, thread):
		return self.create(sender = sender, content = content, thread = thread)
	def copy_message(self, owner, messagecopied, message):
		return self.create(owner = owner, messagecopied=messagecopied, message = message)

class MessageThread(models.Model):
	subject = models.CharField(max_length=128)
	participants = models.ManyToManyField(User, related_name = 'message_threads')

	def __str__(self):              # __unicode__ on Python 2
		return self.subject

class Message(models.Model):
	sender = models.ForeignKey(User, related_name='sender' )
	thread = models.ForeignKey(MessageThread, related_name='thread')
	when = models.DateTimeField(auto_now_add=True)
	content = models.TextField(null = True, blank = True)

	objects = MessageManager()

	def __str__(self):              # __unicode__ on Python 2
		return '{} by {} on {}'.format(self.content, self.sender, self.when)

class CopyMessage(models.Model):
	owner = models.ForeignKey(User, related_name='owner' )
	message = models.ForeignKey(MessageThread, on_delete=models.CASCADE)
	messagecopied = models.TextField(null = True, blank = True)
	when = models.DateTimeField(auto_now_add=True)

	objects = MessageManager()

	def __str__(self):
		return '{} by {} on {}'.format(self.messagecopied, self.owner, self.when)



