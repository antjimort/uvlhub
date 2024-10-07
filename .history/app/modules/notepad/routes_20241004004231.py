from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

from app.modules.notepad import notepad_bp


@notepad_bp.route('/notepad', methods=['GET'])
def index():
    return render_template('notepad/index.html')
