import media  # import our media.py with Movie class in it
from fresh_tomatoes import open_movies_page  # import the HTML creation code

# toy_story == new instance of Movie
toy_story = media.Movie(
    'Toy Story',
    "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SY1000_SX670_AL_.jpg',
    'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie(
    'Avatar',
    "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg',
    'https://www.youtube.com/watch?v=5PSNL1qE6VY')

pretty_woman = media.Movie(
    'Pretty Woman',
    "A man in a legal but hurtful business needs an escort for some social events, and hires a beautiful prostitute he meets... only to fall in love.",
    'https://images-na.ssl-images-amazon.com/images/M/MV5BNjk2ODQzNDYxNV5BMl5BanBnXkFtZTgwMTcyNDg4NjE@._V1_SY1000_CR0,0,660,1000_AL_.jpg',
    'https://www.youtube.com/watch?v=Ng2hEIWVqqo')

inside_out = media.Movie(
    'Inside Out',
    "After young Riley is uprooted from her Midwest life and moved to San Francisco, her emotions - Joy, Fear, Anger, Disgust and Sadness - conflict on how best to navigate a new city, house, and school.",
    'https://images-na.ssl-images-amazon.com/images/M/MV5BOTgxMDQwMDk0OF5BMl5BanBnXkFtZTgwNjU5OTg2NDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
    'https://www.youtube.com/watch?v=seMwpP0yeu4')

spotlight = media.Movie(
    'Spotlight',
    "The true story of how the Boston Globe uncovered the massive scandal of child molestation and cover-up within the local Catholic Archdiocese, shaking the entire Catholic Church to its core.",
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMjIyOTM5OTIzNV5BMl5BanBnXkFtZTgwMDkzODE2NjE@._V1_SY1000_CR0,0,676,1000_AL_.jpg',
    'https://www.youtube.com/watch?v=EwdCIpbTN5g')

the_martian = media.Movie(
    'The Martian',
    "An astronaut becomes stranded on Mars after his team assume him dead, and must rely on his ingenuity to find a way to signal to Earth that he is alive.",
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_SY1000_CR0,0,675,1000_AL_.jpg',
    'https://www.youtube.com/watch?v=ej3ioOneTy8')

# Create movies array
movies = [toy_story, avatar, pretty_woman, inside_out, spotlight, the_martian]

# open_movies_page(movies)
print media.Movie.__doc__  # whatever i defined in the class in triple quotes
print media.Movie.__name__  # the name of the class

# the module, or filename (without the .py) of the class
print media.Movie.__module__
