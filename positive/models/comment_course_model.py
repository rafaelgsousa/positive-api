from django.db import models
from django.utils import timezone

from .course_model import Course
from .user_model import CustomUser


class CommentCourse(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now, blank=True, null=True)
    message=models.CharField(max_length=500)


    def __str__(self):
        return f'User: {self.user} - course: {self.course}'