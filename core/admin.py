from django.contrib import admin
from .models import Movie, Genre, Country, Cinema, Session, Favorite, Review


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'created_by', 'created_at', 'display_genres')
    list_display_links = ('title',)
    search_fields = ('title', 'description')
    list_filter = ('country', 'genres')
    filter_horizontal = ('genres',)
    raw_id_fields = ('created_by',)
    readonly_fields = ('created_at', 'updated_at')

    @admin.display(description="Жанры")
    def display_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'created_at')
    list_display_links = ('name',)
    search_fields = ('name', 'address')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('movie', 'cinema', 'date', 'time', 'format', 'price')
    list_filter = ('cinema', 'movie', 'format', 'date')
    search_fields = ('movie__title',)
    date_hierarchy = 'date'
    raw_id_fields = ('movie', 'cinema')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'added_at')
    list_filter = ('added_at',)
    search_fields = ('user__username', 'movie__title')
    date_hierarchy = 'added_at'
    raw_id_fields = ('user', 'movie')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('user__username', 'movie__title', 'text')
    date_hierarchy = 'created_at'
    raw_id_fields = ('user', 'movie')