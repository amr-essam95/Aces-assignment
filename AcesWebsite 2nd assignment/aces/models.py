from django.db import models



class Slot(models.Model):
    date =models.DateTimeField()
    no_of_slots=models.IntegerField()
    no_of_available_slots=models.IntegerField()

    def __str__(self):
        return str(self.date)

class applicants(models.Model):
    mobile_number =models.CharField(max_length=250)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)

    def __str__(self):
        return self.mobile_number
