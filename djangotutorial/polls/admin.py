from django.contrib import admin
from .models import Choice, Question

# class ChoiceInLine(admin.StackedInline):
# abbreviated version
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # have to chage the name fields -> fieldsets
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)

# Register your models here.
