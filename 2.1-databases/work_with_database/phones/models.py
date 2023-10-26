from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    image = models.CharField(max_length=200)
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name
