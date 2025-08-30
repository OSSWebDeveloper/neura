from django.db import models

class Worker(models.Model):
    CATEGORY_CHOICES = [
        ('Admin', 'Admin'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    ]
    
    name = models.CharField('Ismi', max_length=255)
    password = models.CharField('Paroli', max_length=255)
    category = models.CharField('Kategoriyasi', max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class Group(models.Model):
    teacher = models.ForeignKey(
        Worker,
        on_delete=models.CASCADE,
        related_name="groups",
        limit_choices_to={'category': 'Teacher'}  # only teachers can own groups
    )
    name = models.CharField(max_length=255)
    students_count = models.PositiveIntegerField(default=0)  # Example: 23 ta o‘quvchi
    homeworks_submitted = models.PositiveIntegerField(default=0)  # Yangi maydon

    def __str__(self):
        return f"{self.name} ({self.teacher.name})"
