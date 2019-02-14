from django.shortcuts import render
import datetime, requests as req, os

# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')
    
def bye(request):
    bye_date = (datetime.date(2019, 2, 28) - datetime.date.today()) / datetime.timedelta(days=1)
    return render(request, 'utilities/bye.html', {'bye_date': int(bye_date)})
    
def graduation(request):
    grad_date = (datetime.date(2019, 5, 28) - datetime.date.today()) / datetime.timedelta(days=1)
    return render(request, 'utilities/graduation.html', {'grad_date': int(grad_date)})
    
def imagepick(request):
    return render(request, 'utilities/imagepick.html')

def today(request):
    key = os.getenv('WEATHER_KEY')
    url = f'https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&appid={key}'
    whether = req.get(url).json()
    print(whether)
    return render(request, 'utilities/today.html', {'whether': whether['weather'][0]})
    
def ascii_new(request):
    return render(request, 'utilities/ascii_new.html')

def ascii_make(request):
    text = request.POST.get('text')
    font = request.POST.get('font')
    res = req.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
    return render(request, 'utilities/ascii_make.html', {'result': res.text})

def original(request):
    return render(request, 'utilities/original.html')
    
def translated(request):
    naver_client_id = os.getenv('PAPAGO_KEY')
    naver_client_secret = os.getenv('PAPAGO_CLIENT_ID')
    
    papago_url = 'https://openapi.naver.com/v1/papago/n2mt'
    headers = {
        'X-Naver-Client-Id': naver_client_id,
        'X-Naver-Client-Secret': naver_client_secret
    }
    data = {
        'source': 'ko',
        'target': 'en',
        'text': request.POST.get('sentence')
    }
    res = req.post(papago_url, headers=headers, data=data).json()
    print(res)
    return render(request, 'utilities/translated.html', {'translated': res['message']['result']['translatedText']})
    
    
    