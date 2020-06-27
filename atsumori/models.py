from django.conf import settings
from django.db import models
from django.utils import timezone

class MoriUser(models.Model):
    user_name = models.CharField(max_length = 20)
    equip = models.TextField()
    want = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    fixed_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.fixed_date = timezone.now()
        self.save()

    def __str__(self):
        return self.user_name
