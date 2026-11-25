from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_agent = models.BooleanField(default=False)

    def __str__(self):
        if self.is_agent:
            return f"{self.user.username}(Агент)"
        else:
            return f"{self.user.username} (Клиент)"


class Ticket(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=False)
    STATUS_CHOICES = [('NEW', 'Новая'), ('IN_PROGRESS', 'В работе'), ('CLOSED', 'Закрыта')]
    status = models.CharField(choices=STATUS_CHOICES, default='NEW', max_length=20)
    PRIORITY_CHOICES = [('LOW', 'Низкий'),('MEDIUM', 'Средний'), ('HIGH', 'Высокий')]
    priority = models.CharField(choices=PRIORITY_CHOICES, default='MEDIUM', max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tickets')
    assigned_to = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='assigned_tickets')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name ='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"Комментарий от {self.author.username}."

