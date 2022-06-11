
from multiprocessing import connection
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#connect to database
app.secret_key = '12345678'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'lumpatngabret'
app.config['MYSQL_DB'] = 'data_reservasi'
mysql = MySQL(app)

#input reservasi
@app.route('/', methods=['POST'])
def reservasi():
    if request.method == 'POST':
        nama = request.form['nama']
        tanggal_pesanan = request.form['tanggal_pesanan']
        nomer_kamar = request.form['nomer_kamar']
        jenis_kamar = request.form['jenis_kamar']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO reservasi(nama,tanggal_pesanan, nomer_kamar, jenis_kamar) VALUES (%s, %s, %s, %s)",(nama,tanggal_pesanan, nomer_kamar, jenis_kamar))
        mysql.connection.commit()
        return redirect(url_for('home'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/operator')
def dataPengguna():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM reservasi ORDER BY nomer_kamar ASC")
    tampildata = cur.fetchall()
    cur.close()
    return render_template('operator.html', datapemesan = tampildata)

@app.route('/kamar')
def jenisKamar():
    return render_template('kamar.html')

@app.route('/fasilitas')
def fasilitasKamar():
    return render_template('fasilitas.html')

if __name__ == "__main__":
    app.run(debug=True)