from flask import Flask, render_template
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '498d2c03bb91c036ee755f29a35bed2a'

posts = [
  {
    'author': 'Daniela Flores',
    'title': 'The book about you',
    'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eget velit aliquet libero venenatis ultrices at sit amet felis. Mauris at justo risus. Fusce efficitur imperdiet nunc, at aliquam nisl porttitor vel. Etiam molestie arcu elit, et pulvinar justo varius efficitur. Donec laoreet vehicula augue, eu auctor lectus placerat quis. Cras congue, tellus sit amet malesuada dictum, ligula metus convallis magna, ac fermentum neque elit in massa. Aliquam nec mauris risus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Fusce ipsum nibh, posuere interdum ullamcorper et, iaculis ac nulla. Aliquam erat volutpat. Donec eu dolor.',
    'date_posted': 'November 22, 2019'
  },
  {
    'author': 'Jose Brena',
    'title': 'About cars',
    'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eget velit aliquet libero venenatis ultrices at sit amet felis. Mauris at justo risus. Fusce efficitur imperdiet nunc, at aliquam nisl porttitor vel. Etiam molestie arcu elit, et pulvinar justo varius efficitur. Donec laoreet vehicula augue, eu auctor lectus placerat quis. Cras congue, tellus sit amet malesuada dictum, ligula metus convallis magna, ac fermentum neque elit in massa. Aliquam nec mauris risus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Fusce ipsum nibh, posuere interdum ullamcorper et, iaculis ac nulla. Aliquam erat volutpat. Donec eu dolor.',
    'date_posted': 'November 23, 2019'
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