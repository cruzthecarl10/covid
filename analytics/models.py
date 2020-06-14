from django.db import models


class Cases(models.Model):
    case_code = models.CharField(max_length=20)
    age = models.CharField(max_length=10)
    age_group = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    date_specimen = models.CharField(max_length=50)
    date_result_release = models.CharField(max_length=50)
    date_rep_conf = models.CharField(max_length=50,default='')
    date_died = models.CharField(max_length=50)
    date_recovered = models.CharField(max_length=50)
    removal_type = models.CharField(max_length=30)
    date_rem_rep = models.CharField(max_length=50)
    is_admitted = models.CharField(max_length=30)
    region = models.CharField(max_length=70)
    province = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    city_psgc = models.CharField(max_length=70)
    health_status = models.CharField(max_length=70)
    is_quarantined = models.CharField(max_length=70)
    date_onset = models.CharField(max_length=50)
    is_pregnant = models.CharField(max_length=5)
    validation = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.case_code} with the age {self.age}'

    class Meta:
        ordering = ['date_result_release']


class WorldwideCases(models.Model):
    date = models.CharField(max_length=20)
    case_per_day = models.CharField(max_length=100)


    class Meta:
        ordering = ['date']