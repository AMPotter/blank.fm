from django.contrib import admin
from main.models import ArticlePost, ArtistProfile, FanProfile, ContributerProfile

admin.site.register(ArticlePost)
admin.site.register(ArtistProfile)
admin.site.register(FanProfile)
admin.site.register(ContributerProfile)

# Register your models here.
