persona = {
        "nombre": "Juan",
        "edad": 30,
        "ciudad": "Madrid"
    }

print(persona["nombre"])
# print(persona.get("edad"))
print(persona["edad"])
persona["edad"] = 35
persona["profesion"] = "ingeniero"
print(persona)
persona.pop("ciudad")
print(persona)


# Diccionarios Anidados:
empresa = {"Ventas": {"Juan": 10000, "Ana": 12000},
           "Marketing": {"Luis": 9000}
           }

print(empresa["Ventas"]["Juan"])
empresa["Marketing"]["Pedro"] = 22000

print(empresa)