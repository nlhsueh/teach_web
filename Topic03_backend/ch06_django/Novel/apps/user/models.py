from django.db import models
from django.dispatch import receiver
from common.util.files import handle_file, delete_file

AVATAR_SAVE_PATH = "user/avatar/"

class User(models.Model):

    THEME_CHOICES = (
        (0, 'dark'),
        (1, 'light'),
    )

    username = models.CharField(max_length=20)
    account = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(upload_to=AVATAR_SAVE_PATH, blank=True, null=True)
    theme = models.IntegerField(default=0, choices=THEME_CHOICES)

    def change_theme(self):
        if (self.theme == 0) :
            self.theme = 1
        else:
            self.theme = 0

    def save(self, *args, **kwargs):
        handle_file(self, "avatar", *args, **kwargs)

    def __str__(self):
        return self.account

# delete the file after the object deleted
@receiver(models.signals.post_delete, sender=User)
def auto_delete_file_on_delete(sender, instance: User, **kwargs):
    delete_file(instance.avatar)

class Subscribe(models.Model):
    reader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reader")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")

    def save(self, *args, **kwargs):
        """Toggle the relation"""
        obj = Subscribe.objects.filter(reader=self.reader, author=self.author).first()
        if obj:
            obj.delete()
            return
        super(Subscribe, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.reader.username} subscribes {self.author.username}'
