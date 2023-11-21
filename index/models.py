from django.db import models

# Create your models here.
class ToDoModel(models.Model):
    content = models.CharField(
        max_length=100,
        null=False,
    )
    deadline = models.DateTimeField()
    delete_flg = models.IntegerField(
        default=0,
    )
    update_date = models.DateTimeField(
        auto_now=True,
    )
    def __str__(self):
        return self.content