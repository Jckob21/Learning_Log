from django.db import models

# To modify data used by learning log application:
# 1. Modify models.py
# 2. Call python manage.py makemigrations on learning_logs
# 3. Tell django to migrate the project (python manage.py migrate)
# 4. Add it to the admin models


# Create your models here.
class Topic(models.Model):
    """A topic user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text


class Entry(models.Model):
    """A specific entry learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()

    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Inner class used by Django to determine the usage of the class"""
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model"""
        return f"{self.text[:50]}..."
    