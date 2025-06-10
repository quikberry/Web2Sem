from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название страны")

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Жанр")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    poster = models.ImageField(upload_to='posters/', verbose_name="Постер")
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name="Страна")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Добавил")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return self.title


class Cinema(models.Model):
    name = models.CharField(max_length=200, verbose_name="Кинотеатр")
    address = models.CharField(max_length=300, verbose_name="Адрес")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлён")

    class Meta:
        verbose_name = "Кинотеатр"
        verbose_name_plural = "Кинотеатры"

    def __str__(self):
        return self.name


class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фильм")
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, verbose_name="Кинотеатр")
    date = models.DateField(verbose_name="Дата показа")
    time = models.TimeField(verbose_name="Время показа")
    format = models.CharField(max_length=20, verbose_name="Формат (2D/3D/IMAX)")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    class Meta:
        verbose_name = "Сеанс"
        verbose_name_plural = "Сеансы"

    def __str__(self):
        return f"{self.movie.title} — {self.date} {self.time}"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фильм")
    added_at = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные фильмы"
        unique_together = ('user', 'movie')

    def __str__(self):
        return f"{self.user.username} → {self.movie.title}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фильм")
    rating = models.IntegerField(verbose_name="Оценка")
    text = models.TextField(verbose_name="Отзыв")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"{self.user.username} — {self.movie.title} ({self.rating}/10)"