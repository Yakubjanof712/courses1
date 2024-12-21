from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name="Kurs nomi")
    description = models.TextField(verbose_name="Kurs tavsifi")
    image = models.ImageField(upload_to='courses/', verbose_name="Kurs rasmi")

    def __str__(self):
        return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons", verbose_name="Kurs")
    title = models.CharField(max_length=255, verbose_name="Dars nomi")
    content = models.TextField(verbose_name="Dars tavsifi")
    video_url = models.URLField(verbose_name="Video manzili", blank=True, null=True)

    def __str__(self):
        return self.title
