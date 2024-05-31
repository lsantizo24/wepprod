from django.db import models


#models to create weekly plan
class weeklyPlan(models.Model):
    orderNumber = models.CharField(max_length=70, unique=True)
    orderModel = models.CharField(max_length =100)
    description = models.TextField()
    orderQty = models.IntegerField()
    family = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    finishDate = models.DateField()
    endDate = models.DateField()
    priority = models.IntegerField()
    weeklyNumber = models.IntegerField()


#models to add productions lines
    



#models to post production 

class ProductionData(models.Model):
    line = models.CharField(max_length=255)
    order = models.CharField(max_length=255)
    lot_number = models.CharField(max_length=255)
    hour = models.IntegerField()
    total_production_hour = models.IntegerField()  # Production count for this hour
    total_production = models.IntegerField()  # Cumulative production count
    fail_count = models.IntegerField()  # Number of failed tests for this hour

    def __str__(self):
        return f"Line: {self.line}, Hour: {self.hour}, Total Production (Hour): {self.total_production_hour}"





