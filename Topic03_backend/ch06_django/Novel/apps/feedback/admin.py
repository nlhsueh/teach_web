from django.contrib import admin
from .models import GoodRelation, UserGradeRelation, BookcaseRelation, Discussion, HistoryRelation

class GoodRelationAdmin(admin.ModelAdmin):
    list_display = ('novel', 'user')

class UserGradeRelationAdmin(admin.ModelAdmin):
    list_display = ('novel', 'user', 'grade')

class BookcaseRelationAdmin(admin.ModelAdmin):
    list_display = ('novel', 'user')

class HistoryRelationAdmin(admin.ModelAdmin):
    list_display = ('novel', 'user')

admin.site.register(GoodRelation, GoodRelationAdmin)
admin.site.register(UserGradeRelation, UserGradeRelationAdmin)
admin.site.register(BookcaseRelation, BookcaseRelationAdmin)
admin.site.register(HistoryRelation, HistoryRelationAdmin)
admin.site.register([Discussion])
