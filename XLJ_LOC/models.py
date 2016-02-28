from django.db import models

# Create your models here.


class LocationRecords(models.Model):
    imei = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()
    update_time = models.DateTimeField()

    def __str__(self):
        return 'time:'+self.update_time.strftime('%a, %b %d %H:%M:%S')+',IMEI:'+self.imei+",lon:"+self.longitude.__str__()+',lat:' + \
               self.latitude.__str__()


