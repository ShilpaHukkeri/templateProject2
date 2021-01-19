from django.shortcuts import render
import datetime
def datetimeview(r):
    TodaysDate=datetime.datetime.now()
    h=int(TodaysDate.strftime('%H'))
    if(h<12):
        msg="GOOD MORNING"
    elif(h<15):
        msg="GOOD AFTRNOON"
    elif(h<19):
        msg="GOOD EVENING"
    else:
        msg="GOOD NIGHT"
    d={'datetime':TodaysDate,'message':msg}
    return render(r,'templateApp2/1.html',d)
    
# Create your views here.
