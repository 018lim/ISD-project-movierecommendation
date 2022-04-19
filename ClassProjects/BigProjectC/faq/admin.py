from django.contrib import admin
from faq.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
