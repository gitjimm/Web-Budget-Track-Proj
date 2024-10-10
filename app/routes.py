from flask import render_template, redirect, url_for, flash, request
from app.forms import LoginForm, RegistrationForm, AddTransactionForm 


def register_routes(app):
    @app.route('/')
    def index():
        return render_template("home.html")

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            if username and password:
                flash('Login successful!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Invalid credentials. Please try again.', 'danger')
        return render_template('login.html', form=form)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegistrationForm()
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            email = request.form.get('email')
            if username and password and email:
                flash(f'Account created for {username}!', 'success')
                return redirect(url_for('login'))
            else:
                flash('Please fill in all fields.', 'danger')
        return render_template('register.html', form=form)

    @app.route('/add-transaction', methods=['GET', 'POST'])
    def add_transaction():
        form = AddTransactionForm()
        if request.method == 'POST':
            amount = request.form.get('amount')
            description = request.form.get('description')
            if amount and description:
                flash('Transaction added successfully!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Please fill in all fields.', 'danger')
        return render_template('add_transaction.html', form=form)

    @app.route('/edit-transaction/<int:transaction_id>', methods=['GET', 'POST'])
    def edit_transaction(transaction_id):
        form = AddTransactionForm()
        if request.method == 'POST':
            amount = request.form.get('amount')
            description = request.form.get('description')
            if amount and description:
                flash('Transaction edited successfully!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Please fill in all fields.', 'danger')
        return render_template('edit_transaction.html', form=form, transaction_id=transaction_id)


    


    @app.route('/dashboard')
    def dashboard():
        return render_template('dashboard.html')


    @app.route('/manage-categories')
    def manage_categories():
        return render_template('manage_categories.html')


    @app.route('/reports')
    def reports():
        return render_template('reports.html')
