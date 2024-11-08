
import sqlite3
celulares = [['Apple - Apple iPhone 13 Pro Max 128GB Seminuevo | Entel', 'Precio: $ 559.990', 'APPLE'], ['Celulares - Samsung Galaxy S23 Ultra 5G 512GB | Entel', 'Precio: $ 699.990', 'SAMSUNG'], ['Smartphone Poco X6 Pro 5G 512GB 6.6"" Black Liberado | Paris', 'Tarjeta: $ 319.990', 'XIAOMI'], ['Apple - Apple iPhone 13 128GB | Entel', 'Precio: $ 544.990', 'APPLE'], ['Smartphone Samsung Galaxy S21 Plus 128Gb Negro Reacondicionado | Lider Electrohogar', 'Precio: $ 349.990', 'SAMSUNG'], ['Iphone 14 5G 128Gb Negro | Lider Electrohogar', 'Precio: $ 649.990', 'APPLE'], ['Iphone 16 Pro 5G 128Gb Gris | Lider Electrohogar', 'Precio: $ 1.199.990', 'APPLE'], ['iPhone 11 64GB Negro | Paris', 'Precio: $ 299.990', 'APPLE'], ['Celulares - Samsung Galaxy S21 FE 5G 128GB | Entel', 'Precio: $ 299.990', 'SAMSUNG'], ['Iphone 16 Pro Max 5G 256Gb Dorado | Lider Electrohogar', 'Precio: $ 1.421.389', 'APPLE'], ['Smartphone Galaxy A55 5G 128GB 6.6"" Awesome Lilac Liberado | Paris', 'Tarjeta: $ 319.990', 'SAMSUNG'], ['Apple - Apple iPhone 15 128GB | Entel', 'Precio: $ 784.990', 'APPLE']]
empresas = [
    ["APPLE", "Tim Cook", "2.7 Trillion USD", "Apple Inc. es una multinacional estadounidense que diseña, fabrica y comercializa productos electrónicos, software y servicios. Es conocida por sus innovaciones en el campo de la tecnología con productos como el iPhone, iPad, Mac y su sistema operativo iOS."],
    ["XIAOMI", "Lei Jun", "0.74 Trillion USD", "Xiaomi Corporation es una empresa china que diseña, desarrolla y vende teléfonos inteligentes, productos electrónicos de consumo, y equipos de tecnología de estilo de vida. Xiaomi ha sido una de las compañías más grandes en ventas de teléfonos móviles a nivel global."],
    ["SAMSUNG", "Jae-Yong Lee", "1.9 Trillion USD", "Samsung Electronics es una de las compañías más grandes de tecnología en el mundo, originaria de Corea del Sur. Produce una amplia gama de productos, desde teléfonos inteligentes y electrodomésticos hasta semiconductores y pantallas, siendo un líder en varias de estas áreas."]
]

reviews = [
    ["Apple - Apple iPhone 13 Pro Max 128GB Seminuevo | Entel", 4.5, "Muy buen rendimiento y excelente cámara, aunque esperaba un poco más por el precio."],
    ["Apple - Apple iPhone 15 128GB | Entel", 4.7, "Rápido, fluido y con una cámara excelente. La duración de la batería es bastante buena."],
    ["Celulares - Samsung Galaxy S21 FE 5G 128GB | Entel", 4.1, "Buena relación calidad-precio, pero la cámara podría ser mejor."],
    ["Celulares - Samsung Galaxy S23 Ultra 5G 512GB | Entel", 4.8, "Increíble pantalla y cámara. Ideal para tomar fotos y grabar videos en alta calidad."],
    ["Apple - Apple iPhone 13 128GB | Entel", 4.3, "Rápido y confiable, aunque el espacio de almacenamiento puede quedarse corto."],
    ["Smartphone Samsung Galaxy S21 Plus 128Gb Negro Reacondicionado | Lider Electrohogar", 3.9, "Buen rendimiento, pero la batería dura menos de lo esperado. Aún así, es una buena opción reacondicionada."],
    ["Iphone 14 5G 128Gb Negro | Lider Electrohogar", 4.6, "Gran diseño y excelente cámara. Perfecto para el uso diario y redes sociales."],
    ["Smartphone Poco X6 Pro 5G 512GB 6.6\" Black Liberado | Paris", 4.2, "Gran capacidad y rendimiento por el precio. Perfecto para el día a día."],
    ["Iphone 16 Pro 5G 128Gb Gris | Lider Electrohogar", 4.9, "Increíble, súper rápido y con un diseño hermoso. Lo mejor de Apple hasta ahora."],
    ["iPhone 11 64GB Negro | Paris", 4.0, "A pesar de ser un modelo más antiguo, sigue funcionando de maravilla. Ideal para usuarios básicos."],
    ["Iphone 16 Pro Max 5G 256Gb Dorado | Lider Electrohogar", 5.0, "Espectacular en todo sentido, definitivamente vale cada peso invertido."],
    ["Smartphone Galaxy A55 5G 128GB 6.6\" Awesome Lilac Liberado | Paris", 4.2, "Bonito diseño y buen rendimiento, aunque podría tener una cámara mejor."]
]




Connection = sqlite3.connect('Celulares.db')

cursor = Connection.cursor()

cursor.execute("DROP TABLE IF EXISTS Empresas")
cursor.execute("DROP TABLE IF EXISTS Celulares")
cursor.execute("DROP TABLE IF EXISTS Reviews")
cursor.execute("CREATE TABLE IF NOT EXISTS Empresas (id_empresa INT PRIMARY KEY, nombre VARCHAR(50), CEO VARCHAR(50), capital FLOAT, descripcion VARCHAR(100))")
cursor.execute("CREATE TABLE IF NOT EXISTS Celulares (id_celular INT PRIMARY KEY, modelo VARCHAR(100), precio int, marca int, FOREIGN KEY (marca) REFERENCES Empresas(id_empresa))") 
cursor.execute("CREATE TABLE IF NOT EXISTS Reviews (id_review INT PRIMARY KEY, modelo int, puntaje int, comentario VARCHAR(200), FOREIGN KEY (modelo) REFERENCES Celulares(id_celular))")

for i in range(len(empresas)):
    empresas[i][2] = float((empresas[i][2].replace(" Trillion USD", "")))
    cursor.execute("INSERT INTO Empresas (id_empresa, nombre, CEO, capital, descripcion) VALUES (?, ?, ?, ?, ?)", (i, empresas[i][0], empresas[i][1], empresas[i][2], empresas[i][3]))

res = cursor.execute("SELECT * FROM Empresas")

for i in range(len(celulares)):
    if celulares[i][2]=="APPLE":
        celulares[i][2]=0
    elif celulares[i][2]=="XIAOMI":
        celulares[i][2]=1
    elif celulares[i][2]=="SAMSUNG":
        celulares[i][2]=2
    celulares[i][1] = int(celulares[i][1].replace("Precio: $ ", "").replace(".", "").replace("Tarjeta: $ ", ""))
    cursor.execute("INSERT INTO Celulares (id_celular, modelo, precio, marca) VALUES (?, ?, ?, ?)", (i, celulares[i][0], celulares[i][1], celulares[i][2]))



for i in range(len(reviews)):
    for j in range(len(celulares)):
        if reviews[i][0] == celulares[j][0]:
            cursor.execute("INSERT INTO Reviews (id_review, modelo, puntaje, comentario) VALUES (?, ?, ?, ?)", (i, j, reviews[i][1], reviews[i][2]))
