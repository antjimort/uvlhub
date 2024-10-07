from flask import render_template, redirect, url_for, flash, request


from app.modules.notepad import notepad_bp


@notepad_bp.route('/notepad', methods=['GET'])
def index():
    return render_template('notepad/index.html')
