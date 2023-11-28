from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/calcular_compra', methods=['GET','POST'])
def calcular_compra():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    cantidad = int(request.form['cantidad'])

    precio_unitario = 9000
    total_sin_descuento = cantidad * precio_unitario

    if 18 <= edad <= 30:
        descuento = 0.15
    elif edad > 30:
        descuento = 0.25
    else:
        descuento = 0

    descuento_aplicado = total_sin_descuento * descuento
    total_con_descuento = total_sin_descuento - descuento_aplicado


    return f'''
        Nombre del cliente: {nombre}<br>
        Total sin descuento: ${total_sin_descuento}<br>
        El descuento es: ${descuento_aplicado}<br>
        El total a pagar es de: ${total_con_descuento}
      
    '''


@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/verificar_sesion', methods=['GET','POST'])
def verificar_sesion():
    nombre = request.form['nombre']
    contrasena = request.form['contrasena']

    usuarios = {'juan': 'admin', 'pepe': 'user'}

    if nombre in usuarios and usuarios[nombre] == contrasena:
        if nombre == 'juan':
            return 'Bienvenido Administrador Juan'
        elif nombre == 'pepe':
            return 'Bienvenido Usuario Pepe'
    else:
        return 'USUARIO O CONTRASEÑA INCORRECTAS'

if __name__ == '__main__':
    app.run(debug=True)