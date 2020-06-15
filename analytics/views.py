from django.shortcuts import render
from analytics.models import Cases, WorldwideCases
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models import Count, Case, When



# @login_required
def home(request):
    template_name = 'index.html'

    # total cases
    total_cases = Cases.objects.all()

    

    # total count of cases per date
    total_dates = []
    total_qty = []
    total_query = Cases.objects.filter().values('date_rep_conf').order_by('date_rep_conf').annotate(created_count=Count('case_code'))[1:]
    for total in total_query:
        date = total['date_rep_conf']
        qt = total['created_count']
        total_dates.append(str(date))
        total_qty.append(qt)    

    print(total_query.count())

    total_dates_world = []
    total_qty_world = []
    total_query = WorldwideCases.objects.filter().values('date').order_by('date').annotate(created_count=Sum('case_per_day'))
    for total in total_query:
        date = total['date']
        qt = total['created_count']
        total_dates_world.append(str(date))
        total_qty_world.append(qt)




    # total death count of cases per date
    total_dead = Cases.objects.filter().exclude(date_died__exact='').count()
    print(total_dead)

    total_deaths_qty = []
    total_deaths_dates = []
    total_death_query = Cases.objects.filter().exclude(date_died__exact='').values('date_died').order_by('date_died').annotate(created_count=Count('case_code'))[5:]

    for total in total_death_query:
        date = total['date_died']
        qt = total['created_count']
        total_deaths_dates.append(str(date))
        total_deaths_qty.append(qt)  



    # recovered cases
    total_recovery = Cases.objects.filter().exclude(date_recovered__exact='').count()

    total_recovered_qty = []
    total_recovered_dates = []
    total_recovery_query = Cases.objects.filter().exclude(date_recovered__exact='').values('date_recovered').order_by('date_recovered').annotate(created_count=Count('case_code'))[5:]


    for total in total_recovery_query:
        date = total['date_recovered']
        qt = total['created_count']
        total_recovered_dates.append(str(date))
        total_recovered_qty.append(qt)   



    # cases per location
    place = []
    count = []
    total_case_per_place = Cases.objects.filter().exclude(province__exact='')
    total_case_per_place_query = Cases.objects.filter().exclude(province__exact='').values('province').order_by('province').annotate(created_count=Count('case_code'))[5:]
    for per_place in total_case_per_place_query:
        date = per_place['province']
        qt = per_place['created_count']
        count.append(str(date))
        place.append(qt)   


    # per age
    per_age_count = []
    per_age = []
    total_case_per_age = Cases.objects.filter().exclude(age_group__exact='')
    total_case_per_age_query = Cases.objects.filter().values('age_group').order_by('age_group').annotate(created_count=Count('case_code'))[1:]
    for per_age_z in total_case_per_age_query:
        age = per_age_z['age_group']
        qt = per_age_z['created_count']
        per_age.append(str(age))
        per_age_count.append(qt) 


    # per gender
    per_gender_count = []
    per_gender = []
    total_case_per_age_query = Cases.objects.filter().values('sex').order_by('sex').annotate(created_count=Count('case_code'))
    for per_gender_z in total_case_per_age_query:
        age = per_gender_z['sex']
        qt = per_gender_z['created_count']
        per_gender.append(str(age))
        per_gender_count.append(qt) 
 






    context = {
        'total_cases': total_cases,


        # total cases counts
        'total_dates': total_dates,
        'total_qty': total_qty,

        # total death counts
        'total_deaths_dates': total_deaths_dates,
        'total_deaths_qty': total_deaths_qty,


        # total recovery
        'total_recovered_dates': total_recovered_dates,
        'total_recovered_qty': total_recovered_qty,

        # places
        'place': place,
        'count': count,

        # per age
        'per_age': per_age,
        'per_age_count': per_age_count,


        # per gender
        'per_gender_count': per_gender_count,
        'per_gender': per_gender,


        # total world
        'total_qty_world': total_qty_world,
        'total_dates_world': total_dates_world,


    }

    return render(request,template_name, context=context)