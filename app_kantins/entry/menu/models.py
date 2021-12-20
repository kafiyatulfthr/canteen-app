from app_kantins import db
from app_kantins.entry.menu import views
from flask import request, flash


class listmenu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    timing = db.Column(db.String(200), nullable=False)
    score = db.Column(db.Integer)
    status = db.Column(db.String(200), nullable=False)

    def __init__(self, name, price, calories, status):
        self.content    = name
        self.timing     = price
        self.score      = calories
        self.status     = status
    
    def __repr__(self):
        return '<menu %r>' % self.id

###insert###
def create_menu(content, timing, score, status):
    # Create a dessert with the provided input.
    # At first, we will trust the user.

    # This line maps to line 16 above (the Dessert.__init__ method)
    new_menu = listmenu(content, timing, score, status)

    try:
        # Actually add this dessert to the database
        db.session.add(new_menu)

        # Save all pending changes to the database
        db.session.commit()
        flash('You have successfully created a new menu')
        return new_menu
    except:
        return 'There was an issue adding your menu'

def upload_menu(content, timing, score, status):
    new_menu = listmenu(content, timing, score, status)

    try:
        db.session.add(new_menu)
        db.session.commit()
        return new_menu
    except:
        return 'There was an issue adding your menu'

###update###
def update_menu(id):
    menu = listmenu.query.get_or_404(id)
    try:
        menu.content = request.form['content']
        menu.timing = request.form['timing']
        menu.status = request.form['status']
        db.session.commit()
        return views.index() #ke def di views
    except:
        return 'There was an issue updating your menu'

###delete###
def delete_menu(id):
    menu_to_delete = listmenu.query.get_or_404(id)

    try:
        db.session.delete(menu_to_delete)
        db.session.commit()
        return menu_to_delete
    except:
        return 'There was a problem deleting that menu'

if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print ("Creating database tables...")
    db.create_all()
    print ("Done!")
