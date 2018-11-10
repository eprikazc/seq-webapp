from django.db import models


class Job(models.Model):
    CHOICE_NEW = 'new'
    CHOICE_PROGRESS = 'in_progress'
    CHOICE_SUCCESS = 'success'
    CHOICE_FAILED = 'failed'

    STATUS_CHOICES = [
        (CHOICE_NEW, 'New'),
        (CHOICE_NEW, 'New'),
        (CHOICE_PROGRESS, 'In-Progress'),
        (CHOICE_SUCCESS, 'Success'),
        (CHOICE_FAILED, 'Failed'),
    ]

    input_file = models.FileField()
    output_file = models.FileField(blank=True)
    output_image = models.ImageField(blank=True)
    status = models.CharField(
        max_length=100, choices=STATUS_CHOICES, default=CHOICE_NEW)
    created_at = models.DateTimeField(auto_now_add=True)
