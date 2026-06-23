from django.contrib import admin
from .models import Question, Score

# Simple branding
admin.site.site_header = "Quiz Management System"
admin.site.site_title = "QuizApp Admin Portal"
admin.site.index_title = "Welcome to the Quiz Organizer Dashboard"

# Register only your quiz models
admin.site.register(Question)
admin.site.register(Score)

       

