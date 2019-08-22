from .models import PropertyEnquire
from django.core import serializers

class CreateConversations():

	""" Create User conversations """

	def __init__(self, user_id):
		self.received = list(PropertyEnquire.objects.filter(to_id=user_id, delete_to=False))
		self.sent = list(PropertyEnquire.objects.filter(sender_id=user_id, delete_sender=False))
		self.create_conversations()

	def create_conversations(self):
		self.sorted_conversations = {}
		self.keys = []
		for message in self.received:
			house_id = message.house_id
			conversation_member = message.sender_id
			self.sort_messages(message, house_id, conversation_member)
		for message in self.sent:
			house_id = message.house_id
			conversation_member = message.to_id
			self.sort_messages(message, house_id, conversation_member)
			
		return self.serialize_data()

	def sort_messages(self, message, house_id, conversation_member):
		if self.sorted_conversations.get(f"{house_id}.{conversation_member}"):
			self.sorted_conversations[f"{house_id}.{conversation_member}"].append(message)
		else:
			self.keys.append(f"{house_id}.{conversation_member}")
			self.sorted_conversations[f"{house_id}.{conversation_member}"] = []
			self.sorted_conversations[f"{house_id}.{conversation_member}"].append(message)

		self.sorted_conversations[f"{house_id}.{conversation_member}"].sort(
			key=lambda x: x.posted)

	def serialize_data(self):
		self.serialized_data = []
		for key in self.keys:
			self.serialized_data.append(self.sorted_conversations[key])
		data = [serializers.serialize('json', x) for x in self.serialized_data]
		return data