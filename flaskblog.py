from flask import Flask, render_template
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '498d2c03bb91c036ee755f29a35bed2a'

posts = [
  {
    'author': 'Daniela Flores',
    'title': 'The book about you',
    'content': "No there is no other way, I believe in many ways, I'm trapped in this place. I'm trying to find the light in here, wanting the reasons to be enough, falling in you. Sometimes I cannot forget the path . I want to suffer anymore, no I don't.",
    'date_posted': 'November 22, 2019'
  },
  {
    'author': 'Jose Brena',
    'title': 'About cars',
    'content': "No hay otro camino, confio en los caminos, aunque no sean correctos. Es tan facil no estar solo, pero tan dificil sentirse acompañado. Me da miedo ser juzgado, a enfrentar el fondo de esto. Aunque no te tenga, me tendré a mi. Aunque no sueñe, tu eres lo único que imagino. Y si no te tengo, por lo menos me tendré a mi. No culpes mis estados, mis pecados, mis Amores, mis sentidos y lo que no puedo controlar.",
    'date_posted': 'November 23, 2019'
  },
  {
    'author': 'Luis Breña',
    'title': 'About you',
    'content': "Nunca pienso dos veces, porque tu piensas lo mismo. Todos saben que no siento, pero si no te tengo, por lo menos me tengo a mi. Ya no soy dueño de mi voluntad, de mis pensamientos. Tengo que abrazar el sentimiento, la fuerza del espíritu, mi resplandor. ",
    'date_posted': 'March 16, 2020'
  }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Home')
  
@app.route('/about')
def about():
    return render_template('about.html', title='About')
  
@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register',form=form)
  
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
  
if __name__ == '__main__':
    app.debug = True