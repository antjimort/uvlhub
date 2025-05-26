from flask import render_template, request, redirect, url_for, session
from app.modules.generator import generator_bp

# Paso 1: mostrar formulario o recibir datos del formulario
@generator_bp.route('/generator/step1', methods=['GET', 'POST'])
def step1():
    if request.method == 'POST':
        # Recoger los datos del formulario
        session['num_models'] = request.form.get('num_models_val', 0)
        session['seed'] = request.form.get('seed', 42)
        session['use_seed'] = 'use_seed' in request.form
        session['ensure_satisfiable'] = 'ensure_satisfiable' in request.form
        session['name_prefix'] = request.form.get('name_prefix', '')
        session['feature_count_suffix'] = 'feature_count_suffix' in request.form
        session['constraint_count_suffix'] = 'constraint_count_suffix' in request.form

        # Redirigir al paso 2 (lo implementarás luego)
        return redirect(url_for('generator.step2'))
    return render_template('generator/step1.html')

# Paso 2 (de momento, solo muestra un placeholder)
@generator_bp.route('/generator/step2', methods=['GET'])
def step2():
    return render_template('generator/step2.html')
