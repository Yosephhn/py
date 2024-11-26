import sqlite3

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect('hardware.db')

# Crear un cursor
cur = conn.cursor()

# Crear la tabla
cur.execute('''
CREATE TABLE IF NOT EXISTS hardware (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    requisito TEXT NOT NULL,
    inventario_actual TEXT NOT NULL,
    minimo_recomendado TEXT NOT NULL
)
''')

# Insertar datos de ejemplo
cur.execute('''
INSERT INTO hardware (requisito, inventario_actual, minimo_recomendado) VALUES
('Procesador: Intel Core i3 de 3.4 Ghz o AMD similar', 'Intel Core i5 de 3.6 Ghz', 'Intel Core i3 de 3.4 Ghz'),
('Memoria RAM: 4 GB', '2 GB', '4 GB'),
('Tarjeta gráfica: VRam Intel HD 4000', 'NVIDIA GTX 1050', 'VRam Intel HD 4000'),
('Espacio en disco: 20 GB', '50 GB', '20 GB'),
('Sistema operativo: Windows 7 o superior de 64 bits', 'Windows 10 de 64 bits', 'Windows 7 de 64 bits')
''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()




