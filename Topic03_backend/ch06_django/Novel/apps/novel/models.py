from django.db import models
from django.db.models import Count
from django.dispatch import receiver
from django.utils import timezone
from common.util.files import handle_file, delete_file
from django.core.validators import FileExtensionValidator
from apps.user.models import User

COVER_SAVE_PATH = 'novel/cover/'
CHAPTER_CONTENT_PATH = 'novel/chapter/'


class Novel(models.Model):

    STATE_CHOICES = (
        (0, '連載中'),
        (1, '完結'),
    )

    title = models.CharField(max_length=50)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='work')
    description = models.TextField(max_length=500, blank=True)
    state = models.IntegerField(default=0, choices=STATE_CHOICES)
    cover = models.ImageField(upload_to=COVER_SAVE_PATH)

    def get_good_count(self):
        return self.goodrelation_set.count()

    def get_grade_chart(self):
        grade_chart = {
            "total": 0,
            "count": 0,
            "average": 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0
        }

        grade_chart["count"] = self.usergraderelation_set.count()
        for usergrade in self.usergraderelation_set.all():
            grade_chart["total"] += usergrade.grade
            grade_chart[usergrade.grade] += 1

        if grade_chart["count"] != 0:
            for x in range(1, 6):
                grade_chart[x] /= grade_chart["count"]
                grade_chart[x] *= 100
            grade_chart["average"] = round(
                grade_chart["total"] / grade_chart["count"], 1)

        return grade_chart

    def get_discussion(self):
        return self.discussion_set.order_by("-datetime")

    def get_similar_books(self, count=5):
        """
        查詢和書本A相似最多Tag的前五本書本。

        Args:
            novel_a: 要查詢的書本。

        Returns:
            一個包含前五本書本的列表。
        """
        novel_a_tags = self.tagrelation_set.values_list('tag', flat=True)

        similar_novels = Novel.objects.filter(
            tagrelation__tag__in=novel_a_tags).exclude(id=self.id)

        similar_novels = similar_novels.annotate(
            similar_tags=Count('tagrelation')).order_by('-similar_tags')

        top_five_similar_novels = similar_novels[:count]

        return top_five_similar_novels

    def get_volumn_chapter_dict(self):
        volumns = self.volumn_set.all()
        result = []
        for volumn in volumns:
            chapters = volumn.chapter_set.all()
            result.append({"volumn": volumn, "chapters": chapters})
        return result

    def get_latest_chapter(self):
        # 從小說的所有卷中獲取所有章節
        volumns = self.volumn_set.all()
        latest_chapter = None

        for volumn in volumns:
            # 從每一卷中獲取最新的章節
            chapter = volumn.chapter_set.order_by('-update_date').first()

            # 如果這一卷的最新章節比已知的最新章節更新，則更新最新章節
            if latest_chapter is None or (
                    chapter is not None
                    and chapter.update_date > latest_chapter.update_date):
                latest_chapter = chapter

        return latest_chapter

    def save(self, *args, **kwargs):
        handle_file(self, 'cover', *args, **kwargs)

    def __str__(self):
        return self.title


@receiver(models.signals.post_delete, sender=Novel)
def auto_delete_file_on_delete(sender, instance: Novel, **kwargs):
    delete_file(instance.cover)


class Volumn(models.Model):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.novel.title} {self.title}'


class Chapter(models.Model):
    volumn = models.ForeignKey(Volumn, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    update_date = models.DateTimeField(default=timezone.now)
    word_count = models.IntegerField(default=0)
    content = models.FileField(upload_to=CHAPTER_CONTENT_PATH,
                               validators=[FileExtensionValidator(['txt'])])

    def save(self, *args, **kwargs):
        handle_file(self, "content", *args, **kwargs)

        f = open(self.content.path, "r", encoding="utf8")
        self.word_count = len(f.read())
        super(Chapter, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.volumn.novel.title} {self.volumn.title} {self.title}'


@receiver(models.signals.post_delete, sender=Chapter)
def auto_delete_file_on_delete(sender, instance: Chapter, **kwargs):
    delete_file(instance.content)


class Tag(models.Model):
    tagname = models.CharField(max_length=10)

    def __str__(self):
        return self.tagname


class TagRelation(models.Model):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('novel', 'tag')

    def __str__(self):
        return f'{self.novel.title} {self.tag.tagname}'
