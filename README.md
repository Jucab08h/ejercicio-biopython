Script.py contiene la función summarize_contents la cual recibe la
dirección de un archivo en formato genbank, utiliza os.path.basename para
guardar el nombre del archivo y os.path.dirname para guardar su ruta para 
su posterior impresión. Se imprime el número de records que hace y enlista 
un resumen de cada record hecho, esto con records.append(Seq_Record) 
dentro de un ciclo ford; nos ayudará a repetir el ciclo hasta que no haya
más records que agregar.

para ejecutarlo desde terminal:
	
	python script.py 

en la línea que aparece, ingrese la dirección del archivo en formato genbank 
que desea y de enter para que se muestre un resumen con su nombre, 
dirección, records y una pequeña descripción de cada uno de estos.
