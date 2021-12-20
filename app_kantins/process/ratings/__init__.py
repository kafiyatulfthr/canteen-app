# add views (endpoints) 
from flask import Blueprint

app_ratings = Blueprint('app_ratings', __name__, template_folder='templates', static_folder='static')

from app_kantins.process.ratings import views