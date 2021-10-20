"""
from flask import Blueprint, render_template,request
from handler.user_handler import user_bp
from db_config import mysql
from flask import flash, session, render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
auth = Blueprint('user_bp', __name__)
@auth.route('/submit', methods=['POST'])
def login_submit():
	_email = request.form['inputEmail']
	_password = request.form['inputPassword']
	# validate the received values
	if _email and _password and request.method == 'POST':
		#check user exists
		conn = mysql.connect()
		cursor = conn.cursor()
		sql = "SELECT * FROM tbl_user WHERE user_email=%s"
		sql_where = (_email,)
		cursor.execute(sql, sql_where)
		row = cursor.fetchone()
		if row:
			if check_password_hash(row[3], _password):
				session['email'] = row[1]
				cursor.close()
				conn.close()
				return redirect('/')
			else:
				flash('Invalid password!')
				return redirect('/login')
		else:
			flash('Invalid email/password!')
			return redirect('/login')
"""