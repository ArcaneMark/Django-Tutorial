from django.contrib import admin

# Register your models here.

from .models import Question, Choice

#admin.site.register(Question)
#admin.site.register(Choice)

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date','question_text'] #this will make the pub_date comes before the Question field
    list_display = ('question_text','pub_date','was_published_recently')
    fieldsets = [
        ('Your Question',{'fields':['question_text']}),
        ('Date information',{'fields':['pub_date']}),
    ]

    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)
