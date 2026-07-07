"""Wizard routes — thin Flask controllers.

The wizard state is still stored in Flask session, but the validation,
state updates, persistence and value-building logic live in services.py.
"""

from flask import jsonify, redirect, render_template, request, url_for

from app.modules.generator import generator_bp
from app.modules.generator.services import GeneratorWizardService, WizardRouteResult


def _finish(result: WizardRouteResult):
    if result.redirect_endpoint:
        return redirect(url_for(result.redirect_endpoint))

    return render_template(result.template, **result.context)


# ─── Entry points ────────────────────────────────────────────────────────


@generator_bp.route("/generator", methods=["GET"])
@generator_bp.route("/generator/", methods=["GET"])
def landing():
    GeneratorWizardService.reset_wizard_state()
    return render_template("generator/landing.html")


@generator_bp.route("/generator/random", methods=["GET"])
@generator_bp.route("/generator/random/", methods=["GET"])
def random_entry():
    return redirect(url_for("generator.step1"))


@generator_bp.route("/generator/llm", methods=["GET"])
@generator_bp.route("/generator/llm/", methods=["GET"])
def llm():
    return render_template("generator/llm.html")


# ─── Step 1 · Batch ──────────────────────────────────────────────────────


@generator_bp.route("/generator/random/step1", methods=["GET", "POST"])
def step1():
    if request.method == "POST":
        return _finish(GeneratorWizardService.post_step1(request.form))

    return _finish(GeneratorWizardService.get_step1())


# ─── Step 2 · Language levels ────────────────────────────────────────────


@generator_bp.route("/generator/random/step2", methods=["GET", "POST"])
def step2():
    if request.method == "POST":
        return _finish(GeneratorWizardService.post_step2(request.form))

    return _finish(GeneratorWizardService.get_step2())


# ─── Step 3 · Feature tree ───────────────────────────────────────────────


@generator_bp.route("/generator/random/step3", methods=["GET", "POST"])
def step3():
    if request.method == "POST":
        return _finish(GeneratorWizardService.post_step3(request.form))

    return _finish(GeneratorWizardService.get_step3())


# ─── Step 4 · Constraints ────────────────────────────────────────────────


@generator_bp.route("/generator/random/step4", methods=["GET", "POST"])
def step4():
    if request.method == "POST":
        return _finish(GeneratorWizardService.post_step4(request.form))

    return _finish(GeneratorWizardService.get_step4())


# ─── Step 5 · Attributes ─────────────────────────────────────────────────


@generator_bp.route("/generator/random/step5", methods=["GET", "POST"])
def step5():
    if request.method == "POST":
        return _finish(GeneratorWizardService.post_step5(request.form))

    return _finish(GeneratorWizardService.get_step5())


# ─── Step 6 · Output + download ──────────────────────────────────────────


@generator_bp.route("/generator/random/step6", methods=["GET", "POST"])
def step6():
    if request.method == "POST":
        return _finish(GeneratorWizardService.post_step6(request.form))

    return _finish(GeneratorWizardService.get_step6())


# ─── Pyodide endpoint ────────────────────────────────────────────────────


@generator_bp.route("/generator/random/params-json", methods=["GET"])
def get_params_json():
    payload, status = GeneratorWizardService.get_params_json()
    return jsonify(payload), status


@generator_bp.route("/generator/random/summary-refresh/<int:step>", methods=["POST"])
def refresh_summary(step: int):
    params_dict = GeneratorWizardService.refresh_summary(step, request.form)
    return render_template("generator/_summary_partial.html", params=params_dict)