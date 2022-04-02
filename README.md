# test_redegal
## Funcionamiento
- El script toma el archivo csv que se le especifique por linea de comandos al ejecutarlo y lo transforma en un DataFrame. También transforma el csv que contiene las traducciones de id_localizaciones con sus nombres.
- A partir del DataFrame de datos calcula la distancia necesaria para estar en el percentil 95.
- Crea la query que busca los 10 resultados con mas viajes y la ejecuta dando el resultado por el terminal.

## Librerías
- **Pandas**: Para la ingesta de csv, cálculo de percentil y uso de DataFrames.
- **Pandasql**: Para el uso de queries SQL sobre DataFrames.

## Ejecución
Desde el directorio del proyecto lanzar el siguiente comando:
```sh
python main.py *ruta_csv*
```
### Ejemplo
![image](https://user-images.githubusercontent.com/22099049/161381753-b6fd278b-13c1-4c78-b140-4f4167f126f4.png)
