import pyqrcode
from flask import Flask, flash, render_template, request


app = Flask(__name__, template_folder='./template')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/pyqrcode", methods=['GET','POST'])
def gera_qrcode():

    arquivo = request.form.get('arquivo')
    link = request.form.get('link')


    if request.method=='POST':
        qrcode = pyqrcode.create(link)
        qrcode.png(f"{arquivo}.png", scale=6)

        flash('QRCode gerado com sucesso!')
        print("\nQRCode gerado com sucesso!\n")

    return render_template("home.html")




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)