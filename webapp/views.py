from flask import Flask, render_template, flash, redirect, url_for
from flask.ext.bootstrap import Bootstrap
from webapp.modelos  import *
from webapp.forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "Victor"
bootstrap = Bootstrap(app)
panel_informes = PanelInformes()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def inicio():
    return render_template('/general/inicio.html')


@app.route('/acerca/')
def acerca():
    return render_template('general/acerca.html')


@app.route('/versiones/')
def versiones():
    return render_template('/aplicacion/versiones.html',
                           lista=panel_informes.informar_versiones())


@app.route('/componentes/')
def componentes():
    return render_template('/aplicacion/componentes.html',
                           lista=panel_informes.informar_componentes())


@app.route("/adquisicion/", methods=['GET', 'POST'])
def adquisicion():
    form = SenialForm()
    if form.validate_on_submit():
        try:
            AccionSenial.adquirir(form)
            flash('Se Adquirio la señal')
        except Exception as ex:
            flash("Error: " + str(ex))
        return redirect(url_for('adquisicion'))
    return render_template('aplicacion/adquisicion.html', form=form,
                           seniales=AccionSenial.listar_seniales_adquiridas())

@app.route("/procesamiento/")
def procesamiento():
    return render_template('aplicacion/procesamiento.html')


@app.route("/visualizacion/")
def visualizacion():
    return render_template('aplicacion/visualizacion.html')