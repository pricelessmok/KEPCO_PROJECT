from django.db import models
from django.utils import timezone
from django.contrib import admin
import datetime

class Dataset(models.Model):
    city_id = models.IntegerField(default=0)
    time = models.DateTimeField(default=timezone.now)
    temperature = models.FloatField(default=0)
    rainfall = models.FloatField(default=0)
    windspeed = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    total_traffic = models.FloatField(default=0)

    class Meta:
        unique_together = (('city_id', 'time', 'temperature', 'rainfall', 'windspeed',
                            'humidity', 'total_traffic'))
        ordering = ['time']

    def dic(self):
        fields = [
            'city_id', 'time', 'temperature', 'rainfall', 'windspeed',
            'humidity', 'total_traffic'
        ]
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result

class DatasetAdmin(admin.ModelAdmin):
    list_display = ('city_id', 'time', 'temperature', 'rainfall', 'windspeed',
                            'humidity', 'total_traffic')
    list_per_page = 30

class DataFileUpload(models.Model):
    file = models.FileField()

class DataFileUploadAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        csv_file = request.FILES['file']
        file_data = csv_file.read().decode('utf-8')
        lines = file_data.split('\n')
        for line in lines:
            fields = line.split(",")
            if len(fields) < 3:
                continue
            city_id = int(fields[0] if fields[0] != '' else 0)
            timefield =  str(fields[1] if fields[1] != '' else '0.0.0').split('.')
            time = datetime.date(year=int(timefield[0]), month=int(timefield[1]), day=int(timefield[2]))
            print(time)
            temperature = float(fields[2] if fields[2] != '' else 0)
            rainfall = float(fields[3] if fields[3] != '' else 0)
            windspeed = float(fields[4] if fields[4] != '' else 0)
            humidity = float(fields[5] if fields[5] != '' else 0)
            total_traffic = float(fields[6] if fields[6] != '' else 0)

            Dataset.objects.create(city_id=city_id,
                    time=time, temperature = temperature, rainfall = rainfall,
                    windspeed = windspeed, humidity = humidity, total_traffic = total_traffic)
def save(self, *args, **kwargs):
    super(DataFile, self).save(*args, **kwargs)
    filename = self.data.url