from django.contrib.auth.models import User
from datetime import timedelta
from django.test import TestCase
from django.utils import timezone
from messaging.models import MessageThread, Message, CopyMessage
# Create your tests here.

class MessageThreadModelTestCase(TestCase):


	def setUp(self):
		self.user1 = User.objects.create_user(
			username = 'User1', password ='pass')
		self.user2 = User.objects.create_user(
			username = 'User2', password ='pass')

	def test_thread_create(self):

		self.assertEqual(MessageThread.objects.count(), 0)
		self.assertEqual(self.user1.message_threads.count(), 0)
		self.assertEqual(self.user2.message_threads.count(), 0)

		thread = MessageThread.objects.create(subject='Lunch')
		thread.participants.add(self.user1, self.user2)
		self.assertEqual(MessageThread.objects.count(), 1)
		self.assertEqual(self.user1.message_threads.count(), 1)
		self.assertEqual(self.user2.message_threads.count(), 1)

	def test_message_create(self):
		# """Test creating of message. Find a way to refer `sender`, `content`, `when`"""
		thread = MessageThread.objects.create(subject='LUNCH!!!')
		Message.objects.add_message(
			sender=self.user1, content='guys, ikuzo!\n', thread = thread)
		self.assertEqual(Message.objects.count(), 1)

		Message.objects.add_message(
			sender=self.user2, content ='Sugoi!\n', thread = thread)
		self.assertEqual(Message.objects.count(), 2)

		mess = MessageThread.objects.create(subject='CHANGE TOPIC')

		Message.objects.add_message(
			sender=self.user1, content='hey\n', thread = mess)
		self.assertEqual(Message.objects.count(), 3)
		
		print (Message.objects.all())

	def test_message_copy(self):
		mess = MessageThread.objects.create(subject='CHANGE TOPIC')
		_instance = Message.objects.add_message(sender=self.user1, content='hey\n', thread = mess)

		instance = CopyMessage.objects.copy_message(owner = self.user1, messagecopied='hey\n', message = mess)
		
		self.assertEqual(_instance.content, instance.messagecopied)

		_instance.delete()


		print (Message.objects.all())
		print (CopyMessage.objects.all())




		"""Test creating of message now providing a copy to each recipient.
		When a message is marked removed we don't really remove the Message
		instance but only the user's copy of that instance.
		A user copy may have `owner`, `message`, `thread` and a boolean `is_removed`
		"""
		# thread = Nessage.objects.

