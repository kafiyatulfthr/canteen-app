from flask import render_template, request, Response
from app_kantins import db
from app_kantins.entry.menu import models
from app_kantins.exit.reports import app_reports

import io
import csv

# ############
# ## Update ##
# ## Rating ##
# ############
# @app.route('/updatescore/<int:id>', methods=['GET', 'POST'])
# def updatescore(id):
#     menu = models.listmenu.query.get_or_404(id)
#     if request.method == 'POST':
#         return update_score(id)
#     else:
#         return render_template('score_update.html', menu=menu)

###Report###
@app_reports.route('/report')
def report():
    menus = models.listmenu.query.order_by(models.listmenu.id).all()
    return render_template('reports/report.html', menus=menus)

########################################################################
#WRITE database into a file
@app_reports.route('/download')
def download():
    menu = db.session.query(models.listmenu.id, models.listmenu.content, models.listmenu.timing, models.listmenu.score, models.listmenu.status)
    
    output = io.StringIO()
    writer = csv.writer(output)
    
    line=['id', 'menu', 'timing', 'score', 'status']
    #line = ['id, menu, timing, score, status'] #header pakai koma
    writer.writerow(line)
    
    for row in menu:
        writer.writerow(row)
    
    output.seek(0)
    
    return Response(output, mimetype="text/csv", headers={"Content-Disposition":"attachment;filename=data_makan.csv"})
