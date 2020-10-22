"""
routes.py
====================================
The url routes that render html templates, and handles forms and database manipulation
"""


from __future__ import print_function
from flask import current_app as app
from flask import render_template, url_for, redirect
from .. import db
from ..forms.InternshipForm import InternshipForm
from ..models.Internship import Internship


@app.route('/add_internship', methods=['GET', 'POST'])
def add_internship():
    form = InternshipForm()
    if form.validate_on_submit():
        internship = Internship(company=form.company.data, term=form.term.data, year=form.year.data, location=form.location.data,
                                additional_info=form.additional_information.data)
        db.session.add(internship)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_internship.html', form=form, title='Add Int')


@app.route('/internships')
def internships():
    internships = db.session.query(Internship).all()
    return render_template('internships.html', internships=internships)
