from django.contrib import admin
from django.urls import path, include
from quiz import views

# Custom admin branding
admin.site.site_header = "Quiz Management System"
admin.site.site_title = "QuizApp Admin Portal"
admin.site.index_title = "Welcome to the Quiz Organizer Dashboard"

urlpatterns = [
    path('', views.portal_view, name='portal'),   # Portal page
    path('quiz/', include('quiz.urls')),          # Quiz routes
    path('admin/', admin.site.urls),              # Admin panel
]
