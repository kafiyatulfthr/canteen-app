# add views (endpoints) 
from flask import Blueprint

app_menu = Blueprint('app_menu', __name__, template_folder='templates', static_folder='static')

from app_kantins.entry.menu import views, models