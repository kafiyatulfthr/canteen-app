# add views (endpoints) 
from flask import Blueprint

app_reports = Blueprint('app_reports', __name__, template_folder='templates', static_folder='static')

from app_kantins.exit.reports import views