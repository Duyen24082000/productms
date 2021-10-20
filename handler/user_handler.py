"""
from flask import Blueprint, render_template
user_bp = Blueprint('user_bp', __name__)
@user_bp.route('/login')
def login():
	return render_template('login.html')
"""
