from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Trail
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        trail_name = request.form.get('trail_name')
        date = request.form.get('date')
        
        mileage = request.form.get('mileage')
        time = request.form.get('time')
        notes = request.form.get('notes')

        new_trail = Trail(trail_name=trail_name, date=date, mileage=mileage, time=time, notes=notes)
        db.session.add(new_trail)
        db.session.commit()
        flash('Trail added!', category='success')
    return render_template("home.html", user=current_user)

@views.route('/delete-trail', methods=['POST'])
def delete_trail():
    trail = json.loads(request.data)
    trailId = trail['trailId']
    trail =Trail.query.get(trailId)
    if trail:
        if trail.user_id == current_user.id:
            db.session.delete(trail)
            db.session.commit()
    return jsonify({})

@views.route('/feed')
@login_required
def show_feed():
    return render_template("feed.html", user=current_user)