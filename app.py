from flask import Flask, request, jsonify, render_template

from models import Cupcake, db, connect_db

from forms import AddCakeForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)
def_image = 'https://tinyurl.com/demo-cupcake'


@app.route('/')
def home():
    cakes = Cupcake.query.all()
    form = AddCakeForm()
    return render_template('index.html', cakes=cakes, form=form)


@app.route('/api/cupcakes')
def list_cupcakes():
    all_cakes = [cake.serialize() for cake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cakes)


@app.route('/api/cupcakes/<int:id>')
def get_cake(id):
    cake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cake.serialize())


@app.route('/api/cupcakes', methods=['POST'])
def create_cake():
    """ Post cake """
    # make sure to put placeholder image in if none provided
    img = request.json.get("image", def_image)
    new_cake = Cupcake(flavor=request.json["flavor"], size=request.json["size"],
                       rating=request.json["rating"], image=img)
    db.session.add(new_cake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cake.serialize())
    return (response_json, 201)


@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    cake = Cupcake.query.get_or_404(id)
    """ Below is shorter line that works but lines kept in are to demonstrate things further  """
    db.session.query(Cupcake).filter_by(id=id).update(request.json)
    # todo.title = request.json.get('title', todo.title)
    # todo.done = request.json.get('done', todo.done)
    db.session.commit()
    return jsonify(cupcake=cake.serialize())


@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    cake = Cupcake.query.get_or_404(id)
    db.session.delete(cake)
    db.session.commit()
    return jsonify(message='deleted')
