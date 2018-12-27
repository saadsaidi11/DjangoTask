from django.db import models
from django.shortcuts import render, redirect
from .models import AppDetails, UserDetails
from .forms import AppDetailForm
from django.db.models import Count


# Create your views here.

def list_userDetails(request, idss):
	userIdList = AppDetails.objects.values_list('userId', flat=True)
	if idss not in userIdList: return None
	
	Query = AppDetails.objects.filter(userId=idss)
	applicationsList = Query.values_list('app', flat=True)
	timestampList = Query.values_list('timestamp', flat=True)
	dateList = []
	for x in timestampList:
		 dateList.append(x[:10])

	def most_common(lst):	 
		mydict = {}
		cnt, itm = 0, ''
		for item in reversed(lst):
			 mydict[item] = mydict.get(item, 0) + 1
			 if mydict[item] >= cnt :
				 cnt, itm = mydict[item], item
		return itm
	try:
		result = UserDetails.objects.get(userId=idss)
		result.app_launched = len(set(applicationsList))
		result.most_active_day_last_7_days = most_common(dateList)
		result.number_of_days_active_last_7_days=len(set(dateList))
		result.most_launched_app_last_7_days= most_common(applicationsList)
		result.save()
	except UserDetails.DoesNotExist:
		result = UserDetails(userId= idss, 
		app_launched=len(set(applicationsList)),
		most_active_day_last_7_days=most_common(dateList),
		number_of_days_active_last_7_days=len(set(dateList)),
		most_launched_app_last_7_days= most_common(applicationsList))
		result.save()
	userDetails = UserDetails.objects.get(userId=idss)
	return render(request, 'UserDetails.html', {'UserDetails': userDetails} )


def list_appDetails(request):
	appDetails = AppDetails.objects.all()
	return render(request, 'AppDetails.html', {'AppDetails': appDetails} )


def create_appDetails(request):
	form = AppDetailForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('list_appDetails')

	return render(request, 'AppDetails-form.html', {'form': form})
