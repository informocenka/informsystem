from django.db import models

class ObjectFlat (models.Model):
    ZONE= (
        ('Автозаводский', 'Автозаводский'),
        ('Канавинский', 'Канавинский'),
        ('Ленинский', 'Ленинский'),
        ('Московский', 'Московский'),
        ('Нижегородский', 'Нижегородский'),
        ('Приокский', 'Приокский'),
        ('Советский', 'Советский'),
        ('Сормовский', 'Сормовский'),
    )
    zone = models.CharField(max_length=20, choices=ZONE, default='Автозаводский')

    ROOMS = (
        ('1 комната', '1 комната'),
        ('2 комнаты', '2 комнаты'),
        ('3 комнаты', '3 комнаты'),
        ('более 3 комнат', 'более 3 комнат'),
    )
    rooms = models.CharField(max_length=20, choices=ROOMS, default='1 комната')

    #Этажность

    FLOOR = (
        ('первый этаж', 'первый этаж'),
        ('средний этаж', 'средний этаж'),
        ('последний этаж', 'последний этаж'),
    )
    floor = models.CharField(max_length=20, choices=FLOOR, default='первый этаж')

    WALL_MATERIAL = (
        ('кирпич','кирпич'),
        ('панель', 'панель'),
        ('нет данных', ''),
    )
    wall_material = models.CharField(max_length=20, choices=WALL_MATERIAL, default='нет данных')

    REMONT = (
        ('дизайнерский проект', 'дизайнерский проект'),
        ('евроремонт', 'евроремонт'),
        ('типовой', 'типовой'),
        ('требуется', 'требуется'),
    )
    remont = models.CharField(max_length=20, choices=REMONT, default='типовой')

    PARKING = (
        ('во дворе', 'во дворе'),
        ('нет', 'нет'),
        ('нет данных', '')
    )
    parking = models.CharField(max_length=20, choices=PARKING, default='нет данных')


    LIFT = (
        ('есть', 'есть'),
        ('нет', 'нет'),
        ('нет данных', ''),
    )
    lift = models.CharField(max_length=20, choices=LIFT, default='нет данных')


class Table(models.Model):
    ZONE = (
        ('AU', 'Автозаводский'),
        ('KNV', 'Канавинский'),
        ('LEN', 'Ленинский'),
        ('MSK', 'Московский'),
        ('NN', 'Нижегородский'),
        ('PRIOK', 'Приокский'),
        ('SOV', 'Советский'),
        ('SOR', 'Сормовский'),
    )
    zone = models.CharField(max_length=20, choices=ZONE, default='AU')

    ROOMS = (
        ('1', '1 комната'),
        ('2', '2 комнаты'),
        ('3', '3 комнаты'),
        ('3+', 'более 3 комнат'),
    )
    rooms = models.CharField(max_length=20, choices=ROOMS, default='1 комната')

    # Этажность

    FLOOR = (
        ('first', 'первый этаж'),
        ('middle', 'средний этаж'),
        ('last', 'последний этаж'),
    )
    floor = models.CharField(max_length=20, choices=FLOOR, default='первый этаж')

    WALL_MATERIAL = (
        ('kirp', 'кирпич'),
        ('pan', 'панель'),
        ('nd', ''),
    )
    wall_material = models.CharField(max_length=20, choices=WALL_MATERIAL, default='нет данных')

    # square
    # building year

    REMONT = (
        ('vip', 'дизайнерский проект'),
        ('euro', 'евроремонт'),
        ('tip', 'типовой'),
        ('nado', 'требуется'),
    )
    remont = models.CharField(max_length=20, choices=REMONT, default='tip')

    PARKING = (
        ('yes', 'во дворе'),
        ('no', 'нет'),
        ('hz', '')
    )
    parking = models.CharField(max_length=20, choices=PARKING, default='hz')

    # BUILD_TYPE =

    LIFT = (
        ('yes', 'есть'),
        ('no', 'нет'),
        ('hz', ''),
    )
    lift = models.CharField(max_length=20, choices=LIFT, default='hz')
    price = models.IntegerField()





