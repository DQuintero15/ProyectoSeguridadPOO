from skimage.metrics import structural_similarity
import cv2
import numpy as np
from math import dist


class DetectorObjetivos:
    def procesarImagenes(plantilla: str, imagen_poligono: str) -> dict:
        # Carga de imagenes
        """
        Lee la imagen y retorna una matriz o numpy array de tres dimensiones (Debido a que tiene colores,
        de otra manera se crearia una matriz de dos dimensiones) mediante la función imread, la cual se
        encarga de darle valores a la matriz de acuerdo a los pixeles de esta y los canales de color.
        Dicha función puede recibir dos parámetros (ruta de imagen, tipo), en donde
        tipo, expresa la forma en que se van a almacenar esta imagenes, es decir, color, escala de grises
        o rgba.
        """
        plantilla = cv2.imread(plantilla)
        ancho1 = plantilla.shape[1]
        largo1 = plantilla.shape[0]
        dimensiones = (ancho1, largo1)

        imagen_poligono = cv2.imread(imagen_poligono)
        ancho2 = imagen_poligono.shape[1]
        largo2 = imagen_poligono.shape[0]

        if (ancho2, largo2) != dimensiones:
            imagen_poligono = cv2.resize(
                imagen_poligono, dimensiones, interpolation=cv2.INTER_AREA
            )

        plantilla_escala_grises = cv2.cvtColor(plantilla, cv2.COLOR_BGR2GRAY)
        imagen_poligono_escala_grises = cv2.cvtColor(
            imagen_poligono, cv2.COLOR_BGR2GRAY
        )

        # Procesamiento de imagenes (SSIM) - The Structural Similarity Index
        # (Medida del índice de similitud estructural).
        """
        structura_similarity: Mide la diferencia perceptiva entre dos imágenes similares. 
        Retorna similitud y diff, los cuales representan el porcentaje de similitud entre las
        dos imagenes procesadas en una escala de grises y una matriz de dos dimensiones con
        las diferencias entre estas respectivamente. 
        Generalmente se usa la escala de grises, ya que permite una "binarización" de estas,
        por tanto, se hace mas facil el reconocimiento preciso de las diferencias. Además, 
        se tendría para analizar un numpy ndarray de dos dimensiones, el cual, computacionalmente
        representa menos cantidad de procesamiento necesario para su identificación. 
        """
        (similitud, diff) = structural_similarity(
            plantilla_escala_grises, imagen_poligono_escala_grises, full=True
        )

        similitud = round(similitud * 100, 3)
        # Mostrar el porcentaje de simulitud de las imagenes.

        if similitud < 60.0 or similitud == 100:
            print(
                "Error! La imagen ingresada no es válida o se encuentra sin impactos."
            )
            return {}
        else:

            """
            Convertir la matriz que contiene las diferencias entre las imagenes (numpy array
            con rangos entre [0,1]), en una matriz de tridimensional con los valores
            en 8 bits.
            """

            diff = (diff * 255).astype("uint8")
            # Combinación del numpy array para generar uno tridimensional
            matriz_diff = cv2.merge([diff, diff, diff])

            # Aplicación de treshold(umbralización) y contornos

            """
            threshold o umbralización es una función que retorna un numpy array de dos dimensiones
            con las representaciones binarias de las diferencias. Este se vale de dos 
            constantes:
            THRESH_BINARY_INV = Si se encuentra que la matriz en una posición a[i][j][k]
            es mayor al threshold (limite) establecido, entonces se le asigna un valor
            (puede ser blanco), en caso contario, se puede asignar un color negro.
            THRESH_OTSU = Asignar un valor arbitrario óptimo en función a la imagen en caso
            de que no se cumplan con las condiciones de THRESH_BINARY_INV
            """
            thresh = cv2.threshold(
                diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU
            )[1]

            """
            Detección de objetos o contornos.
            Su mayor presición se da a partir de imagenes binarias (En este caso, lo aplicado con threshold).
            """
            contornos = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
            )
            contornos = contornos[0] if len(contornos) == 2 else contornos[1]

            mask = np.zeros(plantilla.shape, dtype="uint8")
            filled_after = imagen_poligono.copy()

            centro = [round(ancho1 // 2), round(largo1 // 1.7)]

            # Mostrar circulo en el centro de la imagen
            cv2.circle(
                imagen_poligono,
                (round(ancho1 // 2), round(largo1 // 1.7)),
                1,
                (255, 69, 0),
                2,
            )
            acomulado_distancias = 0
            for c in contornos:
                area = cv2.contourArea(c)
                if area > 40:
                    x, y, w, h = cv2.boundingRect(c)
                    distancia = dist((centro[0], centro[1]), (x, y))
                    acomulado_distancias += (
                        100 - (distancia * (distancia / 300)) if distancia > 1 else 100
                    )

            efectividad = acomulado_distancias // len(contornos)
            n_impactos = len(contornos)

        estadisticas = {
            "efectivdad": int(efectividad),
            "n_impactos": n_impactos,
        }

        return estadisticas
