from django.db import models
from datetime import datetime

HIGH = 1
MEDIUM = 2
LOW = 3
PRIORITY_CHOICES = [
    (HIGH, 'High'),
    (MEDIUM, 'Medium'),
    (LOW, 'Low'),
]


class NotCompletedTasks(models.Model):
    name = models.CharField(max_length=40)
    priority = models.IntegerField(
        default=HIGH,
        choices=PRIORITY_CHOICES,
    )
    order = models.IntegerField(default=0)
    create_date = models.DateField(default=datetime.now)

    def save(self, *args, **kwargs):
        if self.order == 0:
            if NotCompletedTasks.objects.count():
                latest_model = NotCompletedTasks.objects.latest('order')
                latest_order = latest_model.order
                self.order = latest_order + 1
            else:
                self.order = 1
        super(NotCompletedTasks, self).save()

    def __str__(self):
        return f'{self.id}. {self.name} - {self.priority}'


class CompletedTasks(models.Model):
    name = models.CharField(max_length=40)
    priority = models.CharField(max_length=6)
    complete_date = models.DateField(default=datetime.now)

    def __str__(self):
        return f'{self.id}. {self.name} - {self.priority}'