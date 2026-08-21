from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    # have to chage the name fields -> fieldsets
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]

admin.site.register(Question, QuestionAdmin)

# Register your models here.
