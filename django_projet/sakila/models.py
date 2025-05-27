from django.db import models

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50, unique=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'country'
        ordering = ['country']

    def __str__(self):
        return self.country
    
class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    actors = models.ManyToManyField('Actor', related_name='films', through='FilmActor')
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'film'
        ordering = ['title']
    
    def __str__(self):
        return self.title

    
class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'actor'
        ordering = ['last_name', 'first_name']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class FilmActor(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    class Meta:
        db_table = 'film_actor'
        unique_together = ('film', 'actor')