import os
import json
from datetime import datetime
from typing import List

from flask import Blueprint, render_template, request, flash, jsonify, make_response
from flask_login import login_required, current_user

import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.utils import cloudinary_url

from . import db
from . import cloud_name, cloud_api_key, cloud_api_secret
from .models import Trail, User, TrailMedia

views = Blueprint('views', __name__)

##################################HOME#########################################

@views.route('/')
@login_required
def home():
    return render_template("upload.html", user=current_user)

@views.route('/welcome')
def welcome():
    return render_template("welcome.html", user=current_user)

##################################UPLOAD TRAIL##################################

@views.route('/upload-trail', methods=['GET','POST'])
@login_required
def upload_trail():
    if request.method == 'POST':

        # Parse the request
        payload = request.json

        # Create a new trail and associate with the current user
        new_trail = Trail(**payload)
        current_user.trail.append(new_trail)

        db.session.add(new_trail)

        # Commit the session
        db.session.commit()

        # Success!
        flash('Trail added!', category='success')

        data = {'message': 'Created'}
        return make_response(jsonify(data), 200)

##################################UPLOAD CLOUDINARY##################################

@views.route("/upload-cloudinary", methods=['POST'])
def upload_file():
    #initializing cloudinary with the config
    cloudinary.config(cloud_name=cloud_name, api_key=cloud_api_key, api_secret=cloud_api_secret)
    upload_result = None
    file_to_upload = request.files['file']
    #if there is a file to upload, then upload to cloudinary
    if file_to_upload:
      upload_result = cloudinary.uploader.upload(file_to_upload)
      #could potentially save this image in an image table then associate that image as a relationship to a trail
      return jsonify(upload_result)

#########################VIEW FEED####################################################

@views.route('/feed', methods=['GET', 'POST'])
@login_required
def show_feed():

    trails = current_user.trail

    # user_trails = [trail.to_dict() for trail in trails]
    # trails.sort(key = lambda x:x["date"], reverse=True)

    return render_template("feed.html", user=current_user, trails=trails)

#PHOTO MODAL
@views.route('/api/node/<string:trail_id>')
def show_photo_album(trail_id):
    trail = Trail.query.get(trail_id)
    photo_array = [{'title': x.title, 'url': x.url} for x in trail.images]
    return make_response(jsonify({'photo_array':photo_array}))

#NOTES MODAL
@views.route('/api/notes-modal/<string:trail_id>')
def get_modal_info(trail_id):
    trail = Trail.query.get(trail_id)
    notes_data = {'title': trail.trail_name, 'notes': trail.notes}
    return make_response(jsonify({'notes_data':notes_data}))

#########################CHARTS####################################################

@views.route('/charts', methods=['GET', 'POST'])
@login_required
def view_charts():
    return render_template('charts.html', user=current_user)

@views.route('/trail-chart/<string:attribute>.json', methods=['GET'])
@login_required
def get_trail_chart(attribute: str):

    my_dict = current_user.get_trail_attribute_counts(attribute)
    data = {
        'labels': list(my_dict.keys()),
        'values': list(my_dict.values())
    }
    return jsonify(data)

##############################DELETE##########################################

@views.route('/delete-trail', methods=['POST'])
def delete_trail():
    trail =Trail.query.get(trailId)
    current_user.trails.remove(trail)
    db.session.commit()
    return jsonify({})