from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from AutoBlendSolverV4 import AutoBlendInfo

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blend.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Blend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(200), nullable=False)
    tankvolume = db.Column(db.String(200), default=0)
    actualrvp = db.Column(db.String(200), nullable=False)
    actualvl = db.Column(db.String(200), nullable=False)
    actualt50 = db.Column(db.String(200))
    finalcalc = db.Column(db.String(200))


    def __repr__(self):
        return '<Blend %r>' % self.id


@app.route('/')
def index():
    blends = Blend.query.order_by(Blend.id).all()
    return render_template("index.html", blends=blends)

@app.route('/newblend/', methods=['POST', 'GET'])
def NewBlend():
    if request.method == 'POST':
        newlocation = request.form['newlocation']
        newtankvolume = request.form['newtankvolume']
        newactualrvp = request.form['newactualrvp']
        newactualvl = request.form['newactualvl']
        newactualt50 = request.form['newactualt50']
        new_blend = Blend(location=newlocation, tankvolume=newtankvolume,actualrvp=newactualrvp, actualvl=newactualvl, actualt50=newactualt50)

        try:
            db.session.add(new_blend)
            db.session.commit()
            return redirect('/')
        except:
            return 'the blend didnt save correctly'
    else:
        return render_template("newblend.html")


@app.route('/autocalc/<int:id>')
def Calculate(id):
    blend = Blend.query.get_or_404(id)
    newcalc = AutoBlendInfo(blend.location,blend.tankvolume,blend.actualrvp, blend.actualvl, blend.actualt50)
    blend_bbls = newcalc.final_auto_calc()
    blend.finalcalc = blend_bbls

    try:
        db.session.commit()
        return redirect('/')

    except:
        return 'The blend did not calculate correctly'


@app.route('/delete/<int:id>')
def delete(id):
    blend_to_delete = Blend.query.get_or_404(id)

    try:
        db.session.delete(blend_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem updating the blend'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    blend = Blend.query.get_or_404(id)

    if request.method =='POST':
        blend.location = request.form['location']
        blend.tankvolume = request.form['tankvolume']
        blend.actualrvp = request.form['actualrvp']
        blend.actualvl = request.form['actualvl']
        blend.actualt50 = request.form['actualt50']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your blend'

    else:
        return render_template('update.html', blend=blend)


@app.route('/material_test', methods=['GET', 'POST'])
def material_test():
    return render_template("Material_test.html")

@app.route('/update_targets', methods=['GET', 'POST'])
def update_targets():
    return render_template('update_targets.html')

if __name__ == '__main__':
    app.run()
