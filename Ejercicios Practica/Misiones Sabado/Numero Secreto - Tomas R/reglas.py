
def mostrar_reglas()->None:
    """
    La función imprime la reglas del juego.

    Args:
        None: No recibe ningun argumento.

    Returns:
        None: No retorna ningún valor, simplemente imprime las reglas del juego
    """
    
    reglas = '''
\033[32m🌌 REGLAS DEL JUEGO - EL RETORNO DEL NÚMERO SECRETO 🌌\033[0m

🧙¡Bienvenido, joven Padawan! Estás a punto de embarcarte en una misión muy importante en la galaxia: adivinar el Número Secreto entre 1 y 10.

-Tu misión:

El Consejo Jedi ha generado un Número Secreto utilizando los poderes del Lado Luminoso de la Fuerza. Tu tarea es descubrir ese número.

Tienes \033[32m3\033[0m intentos para adivinarlo. Usa tus sentidos, deja que la Fuerza fluya a través de ti.

\033[32mSi logras adivinar:\033[0m
Serás aclamado como el nuevo héroe de la República y estaras mas cerca de convertirte en un Maestro Jedi.

\033[31mSi fallas:\033[0m
No temas, joven aprendiz. Si no aciertas después de \033[32m3\033[0m intentos, el número secreto será revelado.

🧙¡Que la Fuerza esté contigo en cada elección!'''

    return print(reglas)