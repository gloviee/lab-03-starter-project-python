from spaceship.app import make_app
from spaceship.config import Settings

settings = Settings()
app = make_app(settings)