from flask import render_template, request, redirect
from app_kantins.entry.menu import app_menu, models

import csv
from io import TextIOWrapper

##########
## Home ##
##########
@app_menu.route('/')
def index():

    menus = models.listmenu.query.all() ###

    return render_template('menu/index.html', menus=menus)

############
## Insert ##
############
@app_menu.route('/add', methods=['GET', 'POST'])
def add():

    if request.method == 'GET':
        return render_template('menu/add.html')

    # Because we 'returned' for a 'GET', if we get to this next bit, we must
    # have received a POST

    # Get the incoming data from the request.form dictionary.
    # The values on the right, inside get(), correspond to the 'name'
    # values in the HTML form that was submitted.
    else:
        menu_content = request.form['content']
        meal_time = request.form['timing']
        menu_score = request.form['score']
        menu_status = request.form['status']

        models.create_menu(menu_content, meal_time, menu_score, menu_status)
        return redirect('/')

############
## Upload ##
############
@app_menu.route('/uploadfiles', methods=['POST', 'GET'])
# Get the uploaded files
def uploadfiles():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            models.upload_menu(content=row[0], timing=row[1], score=row[2], status=row[3])
        return redirect('/')
    return render_template('menu/index.html')

############
## Update ##
############
@app_menu.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    menu = models.listmenu.query.get_or_404(id)
    if request.method == 'POST':
    #     content = request.form['content']
    #     timing = request.form['timing']
    #     status = request.form['status']
    #    models.update_menu(id)
        return models.update_menu(id) #ke models
    else:
        return render_template('menu/update.html', menu=menu)

############
## Delete ##
############
@app_menu.route('/delete/<int:id>')
def delete(id):
    models.delete_menu(id)
    return redirect('/')