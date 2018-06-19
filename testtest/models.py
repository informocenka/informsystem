from django.db import models

class ObjectFlat (models.Model):
    ZONE= (
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

    #Этажность

    FLOOR = (
        ('first', 'первый этаж'),
        ('middle', 'средний этаж'),
        ('last', 'последний этаж'),
    )
    floor = models.CharField(max_length=20, choices=FLOOR, default='первый этаж')

    WALL_MATERIAL = (
        ('kirp','кирпич'),
        ('pan', 'панель'),
        ('nd', ''),
    )
    wall_material = models.CharField(max_length=20, choices=WALL_MATERIAL, default='нет данных')

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


    LIFT = (
        ('yes', 'есть'),
        ('no', 'нет'),
        ('hz', ''),
    )
    lift = models.CharField(max_length=20, choices=LIFT, default='hz')


# class Table(models.Model):
#     ZONE = (
#         ('AU', 'Автозаводский'),
#         ('KNV', 'Канавинский'),
#         ('LEN', 'Ленинский'),
#         ('MSK', 'Московский'),
#         ('NN', 'Нижегородский'),
#         ('PRIOK', 'Приокский'),
#         ('SOV', 'Советский'),
#         ('SOR', 'Сормовский'),
#     )
#     zone = models.CharField(max_length=20, choices=ZONE, default='AU')
#
#     ROOMS = (
#         ('1', '1 комната'),
#         ('2', '2 комнаты'),
#         ('3', '3 комнаты'),
#         ('3+', 'более 3 комнат'),
#     )
#     rooms = models.CharField(max_length=20, choices=ROOMS, default='1 комната')
#
#     # Этажность
#
#     FLOOR = (
#         ('first', 'первый этаж'),
#         ('middle', 'средний этаж'),
#         ('last', 'последний этаж'),
#     )
#     floor = models.CharField(max_length=20, choices=FLOOR, default='первый этаж')
#
#     WALL_MATERIAL = (
#         ('kirp', 'кирпич'),
#         ('pan', 'панель'),
#         ('nd', ''),
#     )
#     wall_material = models.CharField(max_length=20, choices=WALL_MATERIAL, default='нет данных')
#
#     # square
#     # building year
#
#     REMONT = (
#         ('vip', 'дизайнерский проект'),
#         ('euro', 'евроремонт'),
#         ('tip', 'типовой'),
#         ('nado', 'требуется'),
#     )
#     remont = models.CharField(max_length=20, choices=REMONT, default='tip')
#
#     PARKING = (
#         ('yes', 'во дворе'),
#         ('no', 'нет'),
#         ('hz', '')
#     )
#     parking = models.CharField(max_length=20, choices=PARKING, default='hz')
#
#     # BUILD_TYPE =
#
#     LIFT = (
#         ('yes', 'есть'),
#         ('no', 'нет'),
#         ('hz', ''),
#     )
#     lift = models.CharField(max_length=20, choices=LIFT, default='hz')
#     price = models.IntegerField()





