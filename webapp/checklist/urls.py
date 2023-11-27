from django.urls import path

from . import views

from .models import Resource

urlpatterns = [
    path("status/", views.status, name="status"),
    path("update_status/", views.update_state, name="update_status"),
    path("load_data/", views.load_data, name="load_data"),
    path("", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES]}),
    path("boss/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[:4]]}),
    path("ash_of_war/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[4:5]]}),
    path("cookbooks/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[5:6]]}),
    path("crystal_tears/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[6:7]]}),
    path("dragon_hearts/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[7:8]]}),
    path("golden_seeds/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[8:9]]}),
    path("key_items/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[9:10]]}),
    path("maps/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[10:11]]}),
    path("merchants/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[11:12]]}),
    path("quests/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[12:13]]}),
    path("sacred_tears/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[13:14]]}),
    path("spirit_summons/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[14:15]]}),
    path("stonework_keys/", views.index, {'category':[item[1] for item in Resource.CATEGORY_CHOICES[15:16]]}),
]