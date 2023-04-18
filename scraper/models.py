from django.db import models

# Create your models here.

from django.db import models

#for storing keyword, made it separate class as we have to give admin access to it
class Keyword(models.Model):
    keyword = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.keyword

#for storing scraped data, made Keyword as foreign key, as it is dependent on keyword
class SearchResult(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE) #keyword field to store for which keyword it is the scraped data
    title = models.CharField(max_length=500) # title of the product
    description = models.TextField() # description of the product
    price = models.DecimalField(max_digits=10, decimal_places=2) # price of the product
    rating = models.DecimalField(max_digits=3, decimal_places=1) # rating of the product
    is_sponsored = models.BooleanField() # check if the product is sponsored or not
    search_date = models.DateField() # the date product was searched and scraped into db

#by default ordered by date 
    class Meta:
        ordering = ('search_date',)

    def __str__(self):
        return f'{self.title} ({self.keyword})'
