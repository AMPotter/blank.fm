from django.contrib import admin
from main.models import ArticlePost, ArtistProfile, FanProfile, ContributerProfile, ArtistPost

admin.site.register(ArticlePost)
admin.site.register(ArtistProfile)
admin.site.register(FanProfile)
admin.site.register(ContributerProfile)
admin.site.register(ArtistPost)

# Register your models here.
