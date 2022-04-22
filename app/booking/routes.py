from flask import Blueprint, render_template
from app import booking
from .models import Dance,Level

blueprint = Blueprint('booking', __name__)

@blueprint.route('/book')
def book():
    return render_template('booking/book.htm')

@blueprint.route('/bookingcomplete')
def bookingcomplete():
    return render_template('booking/bookingComplete.html')

@blueprint.route('/classinfo')
def classinfo():
    return render_template('booking/classInfo.htm')

@blueprint.route('/schedule')
def schedule():
    return render_template('booking/schedule.htm')