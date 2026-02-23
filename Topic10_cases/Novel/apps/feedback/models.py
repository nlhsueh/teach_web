from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.user.models import User
from apps.novel.models import Novel

class Discussion(models.Model):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, editable=False)
    discuss = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.novel.title} {self.user.username} {self.datetime}'

class GoodRelation(models.Model):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """toggle"""
        obj = GoodRelation.objects.filter(novel=self.novel, user=self.user).first()
        if obj:
            obj.delete()
            return
        super(GoodRelation, self).save(*args, **kwargs)

class BookcaseRelation(models.Model):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """toggle"""
        obj = BookcaseRelation.objects.filter(novel=self.novel, user=self.user).first()
        if obj:
            obj.delete()
            return
        super(BookcaseRelation, self).save(*args, **kwargs)

class UserGradeRelation(models.Model):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.IntegerField(default=0, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
    ])

    def save(self, *args, **kwargs):
        """toggle"""
        obj = UserGradeRelation.objects.filter(novel=self.novel, user=self.user, grade=self.grade).first()
        if obj:
            obj.delete()
            return
        super(UserGradeRelation, self).save(*args, **kwargs)
    
class HistoryRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(HistoryRelation, self).save(*args, **kwargs)
