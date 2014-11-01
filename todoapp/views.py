from django.shortcuts import render
from django.utils import timezone
# Create your views here.
def home(request):
	sample_tasks=[
		{
			"time":"17:00",
			"tleft":"1 hour",
			"task":"NETWORKING",
			"desc":"Out to design conference",
		},
		{
			"time":"21:00",
			"tleft":"5 hour",
			"task":"GO TO Solidariy",
			"desc":"At vadakkencherry",
		},
		{
			"time":"23:00",
			"tleft":"7 hour",
			"task":"Go to prayer",
			"desc":"At mosque"
		},		
	]	
	print timezone.now()
	return render(request,'home.html', {'tasks':sample_tasks,'cur_time':timezone.now()})

def calendar(request):
	return render(request,'calendar.html')