from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql

app = Flask(__name__)

# Lógica para crear la tabla en la base de datos
def create_table():
    try:
        # Conectar a la base de datos
        con = sql.connect("Salarios.db")
        
        # Crear un objeto cursor para ejecutar consultas
        cursor = con.cursor()

        # Crear la tabla si no existe
        cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                          Name TEXT,
                          Salary INTEGER)""")
        
        # Guardar los cambios y cerrar la conexión
        con.commit()
        con.close()
        
        print("Tabla creada correctamente.")
    except sql.Error as e:
        print("Error en la base de datos:", e)

# Llamada a la función para crear la tabla
create_table()

# Lógica para actualizar la base de datos
def update_database(supervisor_name, new_salary):
    try:
        # Conectar a la base de datos
        con = sql.connect("Salarios.db")

        # Crear un objeto cursor para ejecutar consultas
        cursor = con.cursor()

        # Ejecutar la actualización
        cursor.execute("UPDATE usuarios SET Salary = ? WHERE Name = ?", (new_salary, supervisor_name))

        # Guardar los cambios y cerrar la conexión
        con.commit()
        con.close()

        print("Salario actualizado correctamente.")
    except sql.Error as e:
        print("Error en la base de datos:", e)

# Ruta para la página principal
@app.route('/')
def index():
    # Aquí deberías obtener los datos de la base de datos y asignarlos a la variable supervisors_data
    supervisors_data = []  # Reemplaza esto con la lógica para obtener los datos reales
    return render_template('salaries.html', supervisors=supervisors_data)

# Ruta para la actualización de salario
@app.route('/update_salary', methods=['POST'])
def update_salary():
    supervisor_name = request.form.get('name')
    new_salary = request.form.get('new_salary')

    # Llamada a la función para actualizar la base de datos
    update_database(supervisor_name, new_salary)

    return redirect(url_for('index'))

# Iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
