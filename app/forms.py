from flask import request, flash

class LoginForm:
    def __init__(self):
        self.email = ''
        self.password = ''

    def validate_on_submit(self):
        if request.method == 'POST':
            self.email = request.form.get('email')
            self.password = request.form.get('password')

            if not self.email or not self.password:
                flash('Email and password are required!', 'danger')
                return False
            
            return True
        return False


class RegistrationForm:
    def __init__(self):
        self.username = ''
        self.email = ''
        self.password = ''
        self.confirm_password = ''

    def validate_on_submit(self):
        if request.method == 'POST':
            self.username = request.form.get('username')
            self.email = request.form.get('email')
            self.password = request.form.get('password')
            self.confirm_password = request.form.get('confirm_password')

            if not self.username or not self.email or not self.password or not self.confirm_password:
                flash('All fields are required!', 'danger')
                return False

            if self.password != self.confirm_password:
                flash('Passwords do not match!', 'danger')
                return False

            return True
        return False


class AddTransactionForm:
    def __init__(self):
        self.amount = ''
        self.category = ''
        self.description = ''

    def validate_on_submit(self):
        if request.method == 'POST':
            self.amount = request.form.get('amount')
            self.category = request.form.get('category')
            self.description = request.form.get('description')

            if not self.amount or not self.category or not self.description:
                flash('All fields are required!', 'danger')
                return False
            
            return True
        return False


