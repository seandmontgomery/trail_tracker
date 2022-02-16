from flask import Blueprint, render_template, request, flash, jsonify, make_response
from flask_login import login_required, current_user
from .models import Trail
from . import db
from . import cloud_name, cloud_api_key, cloud_api_secret
import json
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.utils import cloudinary_url
from datetime import datetime

views = Blueprint('views', __name__)

##################################HOME#########################################

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/welcome')
def welcome():
    return render_template("welcome.html", user=current_user)

##################################UPLOAD TRAIL##################################

@views.route('/upload-trail', methods=['GET','POST'])
@login_required
def upload_trail():
    if request.method == 'POST':
        trail_name = request.json.get('trail_name')
        location = request.json.get('location')
        date = request.json.get('date')
        difficulty = request.json.get('difficulty')
        miles = request.json.get('miles')
        hours = request.json.get('hours')
        minutes = request.json.get('minutes')
        notes = request.json.get('notes')
        image_url = request.json.get('image_url')
        new_trail = Trail(trail_name=trail_name, location=location, date=date, difficulty=difficulty, 
                        miles=miles, hours=hours, minutes=minutes, notes=notes, image_url=image_url)
        db.session.add(new_trail)
        db.session.commit()
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
      upload_result = cloudinary.uploader.upload(file_to_upload, resource_type="auto")
      #could potentially save this image in an image table then associate that image as a relationship to a trail
      return jsonify(upload_result)

#########################CLOUDINARY OPTIMIZATION####################################################

@views.route("/cld_optimize", methods=['POST'])
def cld_optimize():
  app.logger.info('in optimize route')
  cloudinary.config(cloud_name=cloud_name, api_key=cloud_api_key, api_secret=cloud_api_secret)
  if request.method == 'POST':
    public_id = request.form['public_id']
    app.logger.info('%s public id', public_id)
    if public_id:
      cld_url = cloudinary_url(public_id, fetch_format='auto', quality='auto')
      app.logger.info(cld_url)
      return jsonify(cld_url)

#########################VIEW FEED####################################################
      
@views.route('/feed', methods=['GET', 'POST'])
@login_required
def show_feed():
    trails = Trail.query.all()
    return render_template("feed.html", user=current_user, trails=trails)

##############################DELETE##########################################

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