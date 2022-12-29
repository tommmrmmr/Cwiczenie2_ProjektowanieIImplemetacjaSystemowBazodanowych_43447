from django.contrib import admin
from .models import User, Aktor, Rezyser, Film, Ocena

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Aktor)
class AktorAdmin(admin.ModelAdmin):
    pass


@admin.register(Rezyser)
class RezyserAdmin(admin.ModelAdmin):
    pass


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    pass


@admin.register(Ocena)
class OcenaAdmin(admin.ModelAdmin):
    pass

