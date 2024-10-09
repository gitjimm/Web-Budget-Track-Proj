from flask import render_template

def register_routes(app):
    @app.route('/')
    def home():
        return render_template("home.html")

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/dashboard')
    def dashboard():
        return render_template('dashboard.html')

    @app.route('/add-transaction')
    def add_transaction():
        return render_template('add_transaction.html')

    @app.route('/edit-transaction/<int:transaction_id>')
    def edit_transaction(transaction_id):
        return render_template('edit_transaction.html', transaction_id=transaction_id)

    @app.route('/manage-categories')
    def manage_categories():
        return render_template('manage_categories.html')

    @app.route('/reports')
    def reports():
        return render_template('reports.html')