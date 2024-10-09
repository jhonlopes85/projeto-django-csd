from django.http import HttpResponse

# from django.shortcuts import render


def home(request):
    return HttpResponse('''<DOCTYPE>
    <html>
    <head><title>Olá Django</title></head>
    
    <body>
        <h1>Olá Django dnv</h1>
    </body>
                        
                        
                        
</html>                        
''')


def contato(request):
    return HttpResponse('Contato')


def sobre(request):
    return HttpResponse('Sobre')
