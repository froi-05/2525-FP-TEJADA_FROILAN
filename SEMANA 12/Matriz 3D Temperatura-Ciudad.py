def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

temperaturas = [
    [  # Quito
        [  # Semana 1
            {"day": "Lunes", "temp": 70},
            {"day": "Martes", "temp": 72},
            {"day": "Miércoles", "temp": 74},
            {"day": "Jueves", "temp": 73},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 79}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 68},
            {"day": "Martes", "temp": 69},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 69},
            {"day": "Viernes", "temp": 71},
            {"day": "Sábado", "temp": 73},
            {"day": "Domingo", "temp": 74}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 65},
            {"day": "Martes", "temp": 67},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 71},
            {"day": "Sábado", "temp": 72},
            {"day": "Domingo", "temp": 73}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 66},
            {"day": "Martes", "temp": 68},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 72},
            {"day": "Sábado", "temp": 74},
            {"day": "Domingo", "temp": 75}
        ]
    ],
    [  # Guayaquil
        [
            {"day": "Lunes", "temp": 85},
            {"day": "Martes", "temp": 84},
            {"day": "Miércoles", "temp": 83},
            {"day": "Jueves", "temp": 82},
            {"day": "Viernes", "temp": 81},
            {"day": "Sábado", "temp": 80},
            {"day": "Domingo", "temp": 79}
        ],
        [
            {"day": "Lunes", "temp": 88},
            {"day": "Martes", "temp": 87},
            {"day": "Miércoles", "temp": 86},
            {"day": "Jueves", "temp": 85},
            {"day": "Viernes", "temp": 84},
            {"day": "Sábado", "temp": 83},
            {"day": "Domingo", "temp": 82}
        ],
        [
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 89},
            {"day": "Miércoles", "temp": 88},
            {"day": "Jueves", "temp": 87},
            {"day": "Viernes", "temp": 86},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 84}
        ],
        [
            {"day": "Lunes", "temp": 91},
            {"day": "Martes", "temp": 90},
            {"day": "Miércoles", "temp": 89},
            {"day": "Jueves", "temp": 88},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 85}
        ]
    ],
    [  # Cuenca
        [
            {"day": "Lunes", "temp": 60},
            {"day": "Martes", "temp": 61},
            {"day": "Miércoles", "temp": 62},
            {"day": "Jueves", "temp": 63},
            {"day": "Viernes", "temp": 64},
            {"day": "Sábado", "temp": 65},
            {"day": "Domingo", "temp": 66}
        ],
        [
            {"day": "Lunes", "temp": 58},
            {"day": "Martes", "temp": 59},
            {"day": "Miércoles", "temp": 60},
            {"day": "Jueves", "temp": 61},
            {"day": "Viernes", "temp": 62},
            {"day": "Sábado", "temp": 63},
            {"day": "Domingo", "temp": 64}
        ],
        [
            {"day": "Lunes", "temp": 57},
            {"day": "Martes", "temp": 58},
            {"day": "Miércoles", "temp": 59},
            {"day": "Jueves", "temp": 60},
            {"day": "Viernes", "temp": 61},
            {"day": "Sábado", "temp": 62},
            {"day": "Domingo", "temp": 63}
        ],
        [
            {"day": "Lunes", "temp": 56},
            {"day": "Martes", "temp": 57},
            {"day": "Miércoles", "temp": 58},
            {"day": "Jueves", "temp": 59},
            {"day": "Viernes", "temp": 60},
            {"day": "Sábado", "temp": 61},
            {"day": "Domingo", "temp": 62}
        ]
    ]
]

nombres_ciudades = ["Quito", "Guayaquil", "Cuenca"]

for i, ciudad in enumerate(temperaturas):
    for j, semana in enumerate(ciudad):
        suma_celsius = sum(fahrenheit_a_celsius(dia["temp"]) for dia in semana)
        promedio_celsius = suma_celsius / len(semana)
        print(f"Promedio temperatura {nombres_ciudades[i]}, Semana {j+1}: {promedio_celsius:.2f}°C")
