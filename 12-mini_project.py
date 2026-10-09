# Instrucciones:
# Crearás un programa de evaluación de candidatos potenciales con conocimientos en Python para RRHH
# Obtendrás el nombre, años de experiencia y habilidades

# Evaluarás si el candidato:
# - sabe Python/Django, tiene +3 años de experiencia: Candidato óptimo.
# - sabe Python/Django, tiene +1 año de experiencia: Buen Candidato.
# - sabe Python/Django: Posible candidato.
# - no sabe Python: No optimo, se guarda el CV.

# Consejo: Ocupa los métodos .split()

name = input("Nombre: ")
years_experience = int(input("Años de experiencia: "))
skills = input("Introduzca sus habilidades (separadas por ','): ").split(", ")
evaluate_skills = "Python" in skills or "Django" in skills

if evaluate_skills:
    if years_experience >= 3:
        print(f"{name} es un candidato óptimo.")
    elif years_experience >= 1:
        print(f"{name} es un buen candidato.")
    else:
        print(f"{name} es un posible candidato.")
else:
    print("Candidato no óptimo, se guarda CV")
