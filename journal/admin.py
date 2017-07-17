from django.contrib import admin
from journal.models import Journal, JournalImage, JournalYoutube

class JournalImageInline(admin.TabularInline):
    model = JournalImage

class JournalYoutubeInline(admin.TabularInline):
    model = JournalYoutube    

class JournalAdmin(admin.ModelAdmin):
    inlines = [JournalImageInline, JournalYoutubeInline]

admin.site.register(Journal, JournalAdmin)
