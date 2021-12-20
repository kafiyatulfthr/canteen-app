from app_kantins import db
from app_kantins.entry.menu import models 
from flask import request
from app_kantins.process.ratings import views

###update###
def update_score(id):
    menu = models.listmenu.query.get_or_404(id)
    try:
        menu.score = request.form['score']
        db.session.commit()
        return views.scoring()
    except:
        return 'There was an issue updating your menu'