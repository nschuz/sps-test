from datetime import datetime
from mongoengine import Document, StringField, BooleanField, DateTimeField, URLField


class Todo(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    is_active = BooleanField(default =True)
    link = URLField(default='')
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)