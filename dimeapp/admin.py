from django.contrib import admin
from .models import Question, Answer
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('heading', 'body', 'created')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'body', 'created')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
