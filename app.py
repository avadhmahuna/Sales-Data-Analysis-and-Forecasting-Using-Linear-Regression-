from flask import Flask, render_template, request, redirect, send_file, session
import pyodbc
import pandas as pd
import io
from datetime import datetime

app = Flask(__name__)
app.secret_key = "change_this_secret_key"

# -------------------- SQL SERVER CONNECTION --------------------
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=VIAN\\SQLEXPRESS;"
    "DATABASE=my_database;"
    "Trusted_Connection=yes;"
)

# -------------------- LOGIN --------------------
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password'].strip()

        try:
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()

            query = """
                SELECT email, password
                FROM users
                WHERE email = ?
            """

            cursor.execute(query, (email,))
            user = cursor.fetchone()
            conn.close()

        except Exception as e:
            return f"Database Error: {e}"

        # NOTE: plain password check (improve later with hashing)
        if user and user[1] == password:
            session['user'] = email
            return redirect('/dashboard')
        else:
            error = "Invalid Email or Password"

    return render_template('login.html', error=error)


# -------------------- DASHBOARD --------------------
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    if 'user' not in session:
        return redirect('/')

    email = session['user']

    try:
        conn = pyodbc.connect(conn_str)

        query = """
            SELECT sale_id, product_name, quantity, price, sale_date
            FROM sales
            WHERE email_id = ?
            ORDER BY sale_date DESC
        """

        df = pd.read_sql(query, conn, params=[email])
        conn.close()

    except Exception as e:
        return f"Database Error: {e}"

    data = df.to_dict(orient='records')

    # -------------------- DOWNLOAD EXCEL --------------------
    if request.method == 'POST':

        output = io.BytesIO()

        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Sales_Data')

        output.seek(0)

        filename = f"sales_{email}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

        return send_file(
            output,
            download_name=filename,
            as_attachment=True
        )

    return render_template('dashboard.html', data=data)


# -------------------- LOGOUT --------------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


# -------------------- RUN APP --------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)