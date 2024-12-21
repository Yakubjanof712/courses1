from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson
from .forms import CourseForm, LessonForm
from django.shortcuts import render
from .models import Course

# Course update
def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/update_course.html', {'form': form})

# Course delete
def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'courses/delete_course.html', {'course': course})

# Lesson update
def update_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('lesson_list')
    else:
        form = LessonForm(instance=lesson)
    return render(request, 'courses/update_lesson.html', {'form': form})

# Lesson delete
def delete_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        lesson.delete()
        return redirect('lesson_list')
    return render(request, 'courses/delete_lesson.html', {'lesson': lesson})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses})
