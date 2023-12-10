from django.urls import path

from . import views

from .models import Resource

urlpatterns = [
    path("status/", views.status, name="status"),
    path("update_status/", views.update_state, name="update_status"),
    path("load_data/", views.load_data, name="load_data"),
    path("", views.menu, name="menu"),
    path("boss/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[:4]], 'order': 'region'}, name="Bosses"),
    path("ash_of_war/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[4:5]], 'order': 'region'}, name="Ashes of War"),
    path("cookbooks/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[5:6]]}, name="Cookbooks"),
    path("crystal_tears/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[6:7]]}, name="Crystal Tears"),
    path("dragon_hearts/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[7:8]]}, name="Dragon Hearts"),
    path("golden_seeds/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[8:9]]}, name="Golden Seeds"),
    path("key_items/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[9:10]]}, name="Key Items"),
    path("maps/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[10:11]]}, name="Maps"),
    path("merchants/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[11:12]]}, name="Mercahnts"),
    path("quests/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[12:13]]}, name="Quests"),
    path("sacred_tears/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[13:14]]}, name="Sacred Tears"),
    path("spirit_summons/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[14:15]]}, name="Spirit Summons"),
    path("stonework_keys/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[15:16]]}, name="Stonework Keys"),
]