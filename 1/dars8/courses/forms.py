from django import forms
from .models import Course, Lesson

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'image']

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course', 'title', 'content', 'video_url']
