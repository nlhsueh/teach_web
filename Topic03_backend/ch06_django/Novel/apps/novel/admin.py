from django.contrib import admin
from .models import Novel, Volumn, Chapter, Tag, TagRelation

class TagRelationAdmin(admin.ModelAdmin):
    list_display = ('novel', 'tag')

admin.site.register(TagRelation, TagRelationAdmin)
admin.site.register([Novel, Volumn, Chapter, Tag])