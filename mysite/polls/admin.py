from django.contrib import admin
from  .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_filter = ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')

admin.site.register(Question, QuestionAdmin)
