from django.db import models


class Shop(models.Model):
    # Модель Магазина
    name = models.CharField('Название', max_length=20)
    city = models.ForeignKey('city', on_delete=models.PROTECT, blank=True, null=True)
    street = models.ForeignKey('street', on_delete=models.PROTECT, blank=True, null=True)
    house_number = models.IntegerField('Номер дома', blank=True, null=True)
    closeTime = models.TimeField('Время закрытия', blank=True, null=True)
    openTime = models.TimeField('Время открытия', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class City(models.Model):
    # Модель Города
    objects = None
    name = models.CharField('Название', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Street(models.Model):
    # Модель Улицы
    name = models.CharField('Название', max_length=20)
    city = models.ForeignKey('city', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'
