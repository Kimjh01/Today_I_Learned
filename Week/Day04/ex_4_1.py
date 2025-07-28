from conf import settings
from utils.create_url import create_url


result = create_url(settings.NAME, settings.MAIN_URL) 
print(result)