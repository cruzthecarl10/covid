import csv
from analytics.models import Cases, WorldwideCases
from django.conf import settings


path = '/home/carl/pystuff/covid_project/DOH COVID Data Drop_ 20200612 - 04 Case Information.csv'
with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Cases.objects.get_or_create(
                case_code=row[0],
                age=row[1],
                age_group=row[2],
                sex=row[3],
                date_specimen=row[4],
                date_result_release=row[5],
                date_rep_conf=row[6],
                date_died=row[7],
                date_recovered=row[8],
                removal_type=row[9],
                date_rem_rep=row[10],
                is_admitted=row[11],
                region=row[12],
                province=row[13],
                city=row[14],
                city_psgc=row[15],
                health_status=row[16],
                is_quarantined=row[17],
                date_onset=row[18],
                is_pregnant=row[19],
                validation=row[20]
                )
  

path = '/home/carl/pystuff/covid_project/owid-covid-data.csv'
with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = WorldwideCases.objects.get_or_create(
                date=row[3],
                case_per_day=row[5],
                )

  