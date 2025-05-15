import django_setup
from game.models import Game, Genre

genre1 = Genre.objects.create(name="Action")
genre2 = Genre.objects.create(name="Adventure")
genre3 = Genre.objects.create(name="RPG")

game1 = Game.objects.create(title="The Legend of Zelda: Breath of the Wild", year=2017, rating=10.0)
game2 = Game.objects.create(title="The Witcher 3: Wild Hunt", year=2015, rating=9.5)
game3 = Game.objects.create(title="Dark Souls", year=2011, rating=9.0)

game1.genres.add(genre1, genre2)
game2.genres.add(genre1)
game3.genres.add(genre1)
genre3.games.add(game2, game3)

print(game1.genres.all())
print(genre1.games.all())