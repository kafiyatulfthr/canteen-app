from flask import render_template, request
from app_kantins.entry.menu import models
from app_kantins.process.ratings import app_ratings
from app_kantins.process.ratings.models import update_score


## Rating ##
@app_ratings.route('/scoring')
def scoring():
    menus = models.listmenu.query.filter_by(status = 'Active').all()
    return render_template('ratings/scoring.html', menus=menus)

############
## Update ##
## Rating ##
############
@app_ratings.route('/updatescore/<int:id>', methods=['GET', 'POST'])
def updatescore(id):
    menu = models.listmenu.query.get_or_404(id)
    if request.method == 'POST':
        return update_score(id)
    else:
        return render_template('ratings/score_update.html', menu=menu)