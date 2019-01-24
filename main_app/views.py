from django.shortcuts import render
#from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', {'treasures': treasures})

class Treasure:
    def __init__(self, name, value, material, location, img_url):
        self.name = name
        self.value = value
        self.material = material
        self.location = location
        self.image = img_url


treasures = [
    Treasure('Gold Nuggets',1000.00, 'gold', "Curly's creek", 'static/images/gold.jpg'),
    Treasure('Rocks', 0, 'pyrite', "Fall's creek", 'static/images/pyrite.jpg'),
    Treasure('Treasure Chest', 3000.00, 'tin', 'Seattle, WA', 'thumbs.dreamstime.com/z/treasure-chest-11691019.jpg')
]
