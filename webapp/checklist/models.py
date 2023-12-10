from django.db import models

# Create your models here.

class Resource(models.Model):
    found = models.BooleanField(default=False, blank=False)
    location = models.URLField(max_length=255, default='', blank=False)
    name = models.CharField(max_length=255, default='', blank=False)
    CATEGORY_CHOICES = [
        ('BOSS','Boss'),
        ('GREAT BOSS','Great Boss'),
        ('INVASION','Invasion'),
        ('LEGENDARY BOSS','Legendary Boss'),
        ('ASH OF WAR','Ash of war'),
        ('COOKBOOKS','Cookbooks'),
        ('CRYSTAL TEARS','Crystal Tears'),
        ('DRAGON HEARTS','Dragon Hearts'),
        ('GOLDEN SEEDS','Golden Seeds'),
        ('KEY ITEMS','Key Items'),
        ('MAPS','Maps'),
        ('MERCHANTS','Merchants'),
        ('QUESTS','Quests'),
        ('SACRED TEARS','Sacred Tears'),
        ('SPIRIT SUMMONS','Spirit Summons'),
        ('STONESWORD KEYS','Stonesword Keys'),
    ]
    category = models.CharField(max_length=255, default='', blank=False, choices=CATEGORY_CHOICES)
    REGION_CHOICES = [
        ('LIMGRAVE','Limgrave'),
        ('LIURNIA','Liurnia'),
        ('CAELID','Caelid'),
        ('ALTUS PLATEAU','Altus Plateau'),
        ('MOUNTAINTOPS OF THE GIANTS','Mountaintops of the Giants'),
        ('ROUNDTABLE HOLD','Roundtable Hold'),
        ('SIOFRA RIVER','Siofra River'),
        ('AINSEL RIVER','Ainsel River'),
        ('DEEPROOT DEPTHS','Deeproot Depths'),
        ('CRUMBLING FARUM AZULA','Crumbling Farum Azula'),
    ]
    region = models.CharField(max_length=255, default='', blank=False, choices=REGION_CHOICES)
    info = models.CharField(max_length=255, default='', blank=True)

    def getProgress(category=None):
        if (category is not None):
            return (Resource.objects.filter(category__in=category,found=True).count() / Resource.objects.filter(category__in=category).count()) * 100
        return (Resource.objects.filter(found=True).count() / Resource.objects.filter().count()) * 100
    
