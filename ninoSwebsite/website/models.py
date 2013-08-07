from mongoengine import *
import datetime

# Tag sur les photo
class Tag(Document):
	slug = StringField(max_length=255)
	title = StringField(max_length=255)

	def __unicode__(self):
		return self.title

# Modele de photo
class Photo(Document):
	id = StringField(max_length=255,primary_key=True)
	name = StringField(max_length=255)
	shotDate = DateTimeField(default=datetime.datetime.now)
	tags = ListField(Tag)

	def __unicode__(self):
		return self.name



