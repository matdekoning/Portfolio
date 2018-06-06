from django.shortcuts import render, HttpResponse
import urllib
import json
import re



def index(request):
    try:
        new = request.POST.get("post")
        huisOp = request.POST.get("huisOpp")
        perceelOp = request.POST.get("perceelOpp")
        urlPrepGoogle = new.replace(" ", "+")
        url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + urlPrepGoogle +  '&key=AIzaSyBzYHDqf1yrLUwLLiBZfIjV_M8Yz9zjQ0Y'
        data = urllib.request.urlopen(url)
        html = json.loads(data.read())
        dumpen = json.dumps(html)
        adres = dumpen.split(',')
        i = 0
        for item in adres:
            if i ==0:
                if 'lng' in item:
                    lng = item
                    i += 1
                if 'lat' in item:
                    lat = item
        regex = re.compile('[\d.]+')
        lat = re.findall(regex, lat)[0]
        lng = re.findall(regex, lng)[0]


        distanceUrl = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=continental&origins=52.3382516,4.8729215&destinations='+lat+'%2C'+lng+'&key=AIzaSyBzYHDqf1yrLUwLLiBZfIjV_M8Yz9zjQ0Y'
        data = urllib.request.urlopen(distanceUrl)
        html = json.loads(data.read())
        dumpen = json.dumps(html)
        adres = dumpen.split(',')
        i = 0
        for item in adres:
            if i == 0:
                if 'distance' in item:
                    distance = item
                    i += 1
        regex = re.compile('[\d.]+')
        distance = re.findall(regex, distance)[0]

        if float(distance) < 10:
            location = 3
            locationStar= '++'
            locationDes = 'Amsterdam area'
        elif float(distance) >10 and float(distance) < 40:
            location = 2
            locationStar= '+'
            locationDes = 'Near Amsterdam'
        elif float(distance) >40 and float(distance) < 100:
            location = 1.5
            locationStar= '-'
            locationDes = 'Dense area'
        else:
            location = 1
            locationStar= '--'
            locationDes = 'Hinterland'
        postcode = 1234


        if float(perceelOp) < 70:
            perceelRate= '--'
        elif float(perceelOp) >70 and float(perceelOp) < 150:
            perceelRate= '-'
        elif float(perceelOp) >150 and float(perceelOp) < 500:
            perceelRate= '+'
        else:
            perceelRate= '++'

        if float(huisOp) < 70:
            huisRate= '--'
        elif float(huisOp) >70 and float(huisOp) < 100:
            huisRate= '-'
        elif float(huisOp) >100 and float(huisOp) < 200:
            huisRate= '+'
        else:
            huisRate= '++'

        postcode = 1234

        newPrice = (380000 - 21 * (int(postcode))) - ((120 - int(huisOp)) * 900) - ((220 - int(perceelOp)) * 380)


        return render(request, 'huis.html', {'lng':lng, 'lat':lat, 'adres':new, 'prediction':newPrice,'perceelRate':perceelRate,'huisRate':huisRate,'perceelOp':perceelOp, 'locationStar':locationStar, 'locationDes':locationDes, 'huisOp':huisOp})



    except:
        return HttpResponse('A wrong adress type was filled in. <a href="/home"> Please try again</a>. Enter a streetname + streetnumber + city ')
