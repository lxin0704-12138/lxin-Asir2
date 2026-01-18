#!/bin/bash

echo "Introducir el nombre o el modelo de un vehículo"

read name_coche

if [ $name_coche = Renault_Austral ]
then echo "Bien! Me gusta el $name_coche"
elif [ $name_coche = McLaren_P1 ]
then echo "Bien! Me gusta el $name_coche"
elif [ $name_coche = Mercedes-AMG-GTR ]
then echo "Bien! Me gusta el $name_coche"
else echo "Oh, no no me gusta el $name_coche"
fi
