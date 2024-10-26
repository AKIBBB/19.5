from django.contrib import admin

# Register your models here.
from .models import Musician, Album

class AlbumInline(admin.TabularInline):
    model = Album
    extra = 0 

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'instrument_type')
    search_fields = ('first_name', 'last_name', 'email')
    inlines = [AlbumInline]

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = 'Musician Name'  

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_name', 'musician', 'release_date', 'rating')
    list_filter = ('musician', 'rating')
    search_fields = ('album_name',)
