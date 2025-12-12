import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 1080, 1920 

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.SCALED) 
pygame.display.set_caption("Juego de Aprendizaje Móvil")

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (220,220,220)
RED = (255,100,100)
GREEN = (100,255,100)
BLUE = (100,100,255)
LIGHT_BLUE = (200, 200, 255) 

font_big = pygame.font.SysFont("Arial", 80) 
font_mid = pygame.font.SysFont("Arial", 50)
font_small = pygame.font.SysFont("Arial", 40)

clock = pygame.time.Clock()
running = True

STATE_MENU = 0
STATE_SELECT = 1
STATE_GAME = 2
STATE_END = 3
STATE_HELP = 4

state = STATE_MENU

input_text = ""
respuesta_ia = "Escribe tu pregunta y presiona ENTER."

preguntas_algebra = [
("¿Cuál es el valor de x en 2x = 10?", ["3", "5", "10", "2"], 1),
("¿Qué es una incógnita?", ["Una variable", "Un número", "Una suma", "Un signo"], 0),
("5 + 3·2 = ?", ["16", "11", "10", "8"], 1),
("¿Qué es una ecuación?", ["Igualdad", "Restar", "Multiplicar", "Variable"], 0),
("Si x=4, 3x = ?", ["3", "7", "12", "8"], 2),
("¿Qué es un polinomio?", ["Suma de términos", "Número primo", "Raíz", "Fracción"], 0),
("3² = ?", ["6", "9", "3", "12"], 1),
("Una recta es…", ["Curva", "Infinita", "Finita", "Variable"], 1),
("x+x+x = ?", ["2x", "5x", "3x", "x²"], 2),
("¿Qué es factorizar?", ["Sumar", "Reducir", "Multiplicar", "Descomponer"], 3),
("2(x+3) = ?", ["2x+6", "2x+3", "x+5", "6x"], 0),
("Derivada de x²?", ["2x", "x", "x²", "3x"], 0),
("¿Qué es una raíz?", ["Resultado", "Solución", "Número negativo", "Ángulo"], 1),
("7·0 = ?", ["7", "0", "1", "No existe"], 1),
("El opuesto de 5 es…", ["-5", "5", "1/5", "5²"], 0),
("¿Qué es dominio?", ["Entrada", "Salida", "Raíz", "Ángulo"], 0),
("2³ = ?", ["6", "8", "9", "4"], 1),
("Si 4/x = 2 → x = ?", ["2", "8", "3", "4"], 0),
("¿Qué es un sistema?", ["Ecuaciones juntas", "Un número", "Suma", "Ángulo"], 0),
("¿Qué es |x|?", ["Raíz", "Valor absoluto", "Fracción", "Potencia"], 1)
]

preguntas_filosofia = [
("¿Quién dijo “Solo sé que no sé nada”?", ["Sócrates", "Platón", "Aristóteles", "Kant"], 0),
("La filosofía estudia…", ["La verdad", "Los mapas", "La química", "La música"], 0),
("¿Qué es ética?", ["Problemas", "Conducta correcta", "Arte", "Ciencia"], 1),
("Platón creó…", ["El mito de la caverna", "El teléfono", "La rueda", "El libro"], 0),
("¿Qué es pensar?", ["Memorizar", "Reflexionar", "Dormir", "Hablar"], 1),
("Aristóteles fue alumno de…", ["Kant", "Nietzsche", "Platón", "Descartes"], 2),
("La lógica estudia…", ["Belleza", "Razón", "Arte", "Tiempo"], 1),
("¿Qué es moral?", ["Reglas sociales", "Comer", "Escribir", "Viajar"], 0),
("La filosofía nace en…", ["China", "Grecia", "Roma", "India"], 1),
("¿Qué es duda?", ["Certeza", "Investigación", "Inseguridad", "Confianza"], 2),
("Kant habló de…", ["Razón", "Tierra", "Electricidad", "Animales"], 0),
("¿Qué es libertad?", ["Obedecer", "Elegir", "Repetir", "Copiar"], 1),
("Nietzsche habló del…", ["Superhombre", "Átomo", "Cielo", "Sol"], 0),
("¿Qué es verdad?", ["Opinión", "Realidad", "Palabra", "Arte"], 1),
("El mito de la caverna trata de…", ["Ignorancia", "Viajes", "Animales", "Espejos"], 0),
("Descartes dijo…", ["Pienso, luego existo", "Vivo de amor", "Veo y creo", "Llueve"], 0),
("¿Qué es argumento?", ["Razón", "Grito", "Cosa", "Sueño"], 0),
("Estoicismo enseña…", ["Control emocional", "Fuerza física", "Magia", "Canto"], 0),
("¿Qué es duda metódica?", ["Todo se analiza", "Comer", "Correr", "Dormir"], 0),
("Heráclito dijo…", ["Todo fluye", "Nada cambia", "Solo cae", "Todo es igual"], 0)
]

preguntas_dp = [
("¿Qué es autoestima?", ["Valor propio", "Fuerza", "Memoria", "Notas"], 0),
("Dormir bien ayuda a…", ["Motivación", "Odio", "Estrés", "Pereza"], 0),
("La meta es…", ["Objetivo", "Problema", "Frase", "Juego"], 0),
("¿Qué es disciplina?", ["Constancia", "Correr", "Forzar", "Gritar"], 0),
("El estrés se reduce con…", ["Respirar", "Gritar", "Ignorar", "Pelear"], 0),
("Hábito es…", ["Repetición", "Comida", "Ropa", "Juego"], 0),
("Organizar ayuda a…", ["Rendir mejor", "Cansarte", "Olvidar", "Fallar"], 0),
("¿Qué es motivación?", ["Impulso", "Descripción", "Letra", "Fuerza"], 0),
("Leer mejora…", ["Atención", "Problemas", "Sueño", "Hambre"], 0),
("Responsabilidad implica…", ["Cumplir", "Evitar", "Huir", "Ignorar"], 0),
("Perseverar es…", ["Rendirse", "Seguir", "Esperar", "Olvidar"], 1),
("Un líder…", ["Inspira", "Grita", "Ordena", "Ignora"], 0),
("Empatía es…", ["Ponerse en lugar del otro", "Correr", "Hablar", "Dormir"], 0),
("Hábitos malos generan…", ["Problemas", "Salud", "Éxito", "Risa"], 0),
("Ser puntual muestra…", ["Respeto", "Miedo", "Sueño", "Hambre"], 0),
("Leer 10 min diarios es…", ["Hábito", "Juego", "Plan", "Meta"], 0),
("¿Qué es autoconocimiento?", ["Entenderse", "Dormir", "Caminar", "Cantar"], 0),
("Tomar agua mejora…", ["Cuerpo", "Ruido", "Clima", "Arte"], 0),
("Rutina sana implica…", ["Hábitos buenos", "No hacer nada", "Comer mal", "Pelear"], 0),
("¿Qué es resiliencia?", ["Superar dificultades", "Correr", "Saltar", "Leer"], 0)
]

def draw_button(text, x, y, w, h, color):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, border_radius=30) 
    pygame.draw.rect(screen, BLACK, rect, 4, border_radius=30)
    txt = font_mid.render(text, True, BLACK)
    screen.blit(txt, (x + w//2 - txt.get_width()//2,
                      y + h//2 - txt.get_height()//2))
    return rect

particles = []

def spawn_particles(color):
    for _ in range(35):
        particles.append([WIDTH//2, HEIGHT//2,
                          random.randint(-10,10),
                          random.randint(-15,15),
                          color, random.randint(5,10)])

def update_particles():
    for p in particles[:]:
        x,y,vx,vy,color,size = p
        x += vx
        y += vy
        size -= 0.3

        p[0], p[1], p[5] = x, y, size
        pygame.draw.circle(screen, color, (int(x),int(y)), max(1,int(size)))

        if size <= 0:
            particles.remove(p)

teclas_fila1 = list("QWERTYUIOP")
teclas_fila2 = list("ASDFGHJKL")
teclas_fila3 = list("ZXCVBNM")
teclas_fila4 = list("1234567890")

def draw_key(label, x, y, w=80, h=90): 
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, LIGHT_BLUE, rect, border_radius=15)
    pygame.draw.rect(screen, BLACK, rect, 3, border_radius=15)
    
    txt_font = font_small if w < 100 else font_mid
    txt = txt_font.render(label, True, BLACK)
    screen.blit(txt, (x + w//2 - txt.get_width()//2,
                      y + h//2 - txt.get_height()//2))
    return rect

preguntas_actuales = []
categoria = ""
preg_index = 0
puntaje = 0

while running:
    screen.fill(WHITE)
    mx, my = pygame.mouse.get_pos()

    if state == STATE_MENU:

        title = font_big.render("Juego de Aprendizaje", True, BLACK)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 200))

        b1 = draw_button("Iniciar", WIDTH//2 - 400, 500, 800, 180, GRAY)
        b2 = draw_button("Ayuda IA", WIDTH//2 - 400, 800, 800, 180, BLUE)
        b3 = draw_button("Salir", WIDTH//2 - 400, 1100, 800, 180, RED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(mx, my):
                    state = STATE_SELECT
                elif b2.collidepoint(mx, my):
                    state = STATE_HELP
                elif b3.collidepoint(mx, my):
                    running = False

    elif state == STATE_SELECT:

        screen.fill(WHITE)
        title = font_big.render("Elige una categoría", True, BLACK)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 150))

        b1 = draw_button("Álgebra", WIDTH//2 - 400, 400, 800, 180, GRAY)
        b2 = draw_button("Filosofía", WIDTH//2 - 400, 700, 800, 180, GRAY)
        b3 = draw_button("Desarrollo Personal", WIDTH//2 - 400, 1000, 800, 180, GRAY)
        b_back = draw_button("Volver", WIDTH//2 - 400, 1600, 800, 150, RED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if b1.collidepoint(mx, my):
                    categoria = "Álgebra"
                    preguntas_actuales = preguntas_algebra
                    preg_index = 0
                    puntaje = 0
                    state = STATE_GAME

                elif b2.collidepoint(mx, my):
                    categoria = "Filosofía"
                    preguntas_actuales = preguntas_filosofia
                    preg_index = 0
                    puntaje = 0
                    state = STATE_GAME

                elif b3.collidepoint(mx, my):
                    categoria = "Desarrollo Personal"
                    preguntas_actuales = preguntas_dp
                    preg_index = 0
                    puntaje = 0
                    state = STATE_GAME

                elif b_back.collidepoint(mx, my):
                    state = STATE_MENU

    elif state == STATE_GAME:

        pregunta, opciones, correcta = preguntas_actuales[preg_index]

        txt = font_mid.render(f"{categoria}  ({preg_index+1}/20)", True, BLACK)
        screen.blit(txt, (WIDTH//2 - txt.get_width()//2, 80))

        q_rect = pygame.Rect(100, 200, WIDTH - 200, 250)
        pygame.draw.rect(screen, GRAY, q_rect, border_radius=20)
        pygame.draw.rect(screen, BLACK, q_rect, 4, border_radius=20)
        
        q_label = font_mid.render(pregunta, True, BLACK)
        screen.blit(q_label, (q_rect.centerx - q_label.get_width()//2, 
                              q_rect.centery - q_label.get_height()//2))

        btns = []
        y_start = 550 
        
        for i, op in enumerate(opciones):
            b = draw_button(op, WIDTH//2 - 450, y_start + i*280, 900, 180, GRAY) 
            btns.append(b)

        update_particles()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, b in enumerate(btns):
                    if b.collidepoint(mx, my):

                        if i == correcta:
                            puntaje += 1
                            flash_color = GREEN
                            mensaje = "¡Correcto!"
                        else:
                            flash_color = RED
                            mensaje = "Incorrecto"

                        spawn_particles(flash_color)

                        screen.fill(flash_color)
                        msg = font_big.render(mensaje, True, BLACK)
                        screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2))
                        pygame.display.update()
                        pygame.time.delay(350)

                        preg_index += 1
                        if preg_index >= 20:
                            state = STATE_END
                        break

    elif state == STATE_HELP:

        screen.fill((220, 220, 255))

        title = font_big.render("Ayuda de IA", True, BLACK)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 50))

        input_rect = pygame.Rect(50, 200, WIDTH-100, 120)
        pygame.draw.rect(screen, WHITE, input_rect, border_radius=25)
        pygame.draw.rect(screen, BLACK, input_rect, 4, border_radius=25)

        txt = font_mid.render(input_text, True, BLACK)
        screen.blit(txt, (80, 230))
        
        resp_title = font_small.render("Respuesta IA:", True, BLACK)
        screen.blit(resp_title, (80, 360))
        
        resp_line = font_small.render(respuesta_ia, True, BLACK)
        screen.blit(resp_line, (80, 420))


        key_rects = []
        key_w, key_h = 90, 100
        padding = 15
        
        total_width = (key_w * 10) + (padding * 9)
        x_start = (WIDTH - total_width) // 2 
        y_start = 650 

        x = x_start
        for t in teclas_fila1:
            key_rects.append((draw_key(t, x, y_start, key_w, key_h), t))
            x += key_w + padding

        x = x_start + (key_w + padding) // 2
        for t in teclas_fila2:
            key_rects.append((draw_key(t, x, y_start + 120, key_w, key_h), t))
            x += key_w + padding

        x = x_start + (key_w + padding) * 1.5
        for t in teclas_fila3:
            key_rects.append((draw_key(t, x, y_start + 240, key_w, key_h), t))
            x += key_w + padding
        
        y_cmd = y_start + 400
        back_key = draw_key("←", 50, y_cmd, 180, 120)
        space_key = draw_key("⎵", 250, y_cmd, 500, 120)
        enter_key = draw_key("ENTER", 770, y_cmd, 250, 120)

        btn_back = draw_button("Volver al Menú", WIDTH//2 - 400, 1750, 800, 120, (255,180,180))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for rect, label in key_rects:
                    if rect.collidepoint(mx, my):
                        if len(input_text) < 40: 
                            input_text += label
                        break

                if space_key.collidepoint(mx, my):
                    if len(input_text) < 40:
                        input_text += " "

                if back_key.collidepoint(mx, my):
                    input_text = input_text[:-1]

                if enter_key.collidepoint(mx, my):
                    if input_text:
                        respuesta_ia = f"Buscando sobre: {input_text}..." 
                    else:
                        respuesta_ia = "Por favor, escribe algo primero."


                if btn_back.collidepoint(mx, my):
                    input_text = ""
                    respuesta_ia = "Escribe tu pregunta y presiona ENTER."
                    state = STATE_MENU

    elif state == STATE_END:
        screen.fill((240,255,240))

        t1 = font_big.render("¡Juego Terminado!", True, BLACK)
        screen.blit(t1, (WIDTH//2 - t1.get_width()//2, 400))

        t2 = font_big.render(f"Puntaje: {puntaje}/20", True, BLACK)
        screen.blit(t2, (WIDTH//2 - t2.get_width()//2, 700))

        btn_menu = draw_button("Volver al Menú", WIDTH//2 - 400, 1300, 800, 180, BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_menu.collidepoint(mx, my):
                    puntaje = 0
                    preg_index = 0
                    state = STATE_MENU

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
