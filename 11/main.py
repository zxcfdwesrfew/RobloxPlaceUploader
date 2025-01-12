import pygame
import time
import random
from moviepy.editor import VideoFileClip
import numpy as np

# Инициализация pygame
pygame.init()
pygame.mixer.init()  # Инициализация микшера для воспроизведения звука

# Настройка экрана (на весь экран)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Загрузка видео
video_path = r"C:\Users\SystemX\Desktop\1\2.mp4"
clip = VideoFileClip(video_path)

# Загрузка изображения
image_path = r"C:\Users\SystemX\Desktop\1\image.png"
image = pygame.image.load(image_path)

# Загрузка аудио
audio = clip.audio
audio_path = r"C:\Users\SystemX\Desktop\1\audio.wav"  # Временно сохраняем аудио в wav
audio.write_audiofile(audio_path)

# Инициализация pygame mixer для воспроизведения аудио
pygame.mixer.music.load(audio_path)
pygame.mixer.music.play(loops=-1, start=0.0)  # Воспроизводим аудио бесконечно

# Шрифты и символы
fonts = [pygame.font.SysFont("arial", 30), pygame.font.SysFont("arial", 40), pygame.font.SysFont("arial", 50)]
hack_symbols = ["@", "#", "%", "darknet", "onion", ".gov", ".org", ".com"]
error_phrases = ["System Breach Detected!", "Unauthorized Access!", "Critical Error: CABUTO Virus!"]

# Страшные сообщения
virus_jokes = [
    "WARNING: Unauthorized access detected!",
    "ERROR: Data leak detected.",
    "ALERT: Connection to Dark Web established.",
    "Virus detected: CABUTO-64, deleting files..."
]

def generate_virus_joke():
    return random.choice(virus_jokes)

def generate_random_link():
    domain = random.choice(hack_symbols)
    return f"www.{domain}.com"

def generate_random_phone_number():
    country_codes = ['+1', '+44', '+49', '+33', '+7']
    return f"{random.choice(country_codes)} {random.randint(100000000, 999999999)}"

def generate_onion_list():
    return [f"reqest.{random.choice(['onion', 'darknet'])}/{generate_random_phone_number()}" for _ in range(5)]

# Размеры экрана
screen_width, screen_height = screen.get_size()

# Переменные для изображения и .onion ссылок
last_image_time = time.time()
last_generated_time = time.time()
show_onion_list = False
onion_list = []
show_image = False

# Главный цикл
running = True
frame_count = 0
text_move_pos = 0

while running:
    current_time = time.time()

    # Показ изображения каждые 60 секунд на 5 секунд
    if current_time - last_image_time > 60:
        show_image = True
        last_image_time = current_time

    if show_image and current_time - last_image_time > 5:
        show_image = False

    # Генерация новых .onion ссылок каждые 10 секунд
    if current_time - last_generated_time > 10:
        onion_list = generate_onion_list()
        show_onion_list = True
        last_generated_time = current_time

    # Скрытие списка через 20 секунд
    if current_time - last_generated_time > 20:
        show_onion_list = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получение кадра из видео
    frame_time = (frame_count / clip.fps) % clip.duration
    frame = clip.get_frame(frame_time)
    frame_surface = pygame.surfarray.make_surface(np.flipud(frame))
    screen.blit(frame_surface, ((screen_width - frame_surface.get_width()) // 2, (screen_height - frame_surface.get_height()) // 2))

    # Генерация случайных ссылок и текста
    random_text = generate_random_link()
    font = random.choice(fonts)
    text_surface = font.render(random_text, True, pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    screen.blit(text_surface, (random.randint(0, screen_width - text_surface.get_width()), random.randint(0, screen_height - text_surface.get_height())))

    # Вирусные сообщения
    virus_text = generate_virus_joke()
    virus_font = pygame.font.SysFont("arial", 40)
    virus_surface = virus_font.render(virus_text, True, pygame.Color("red"))
    screen.blit(virus_surface, (random.randint(0, screen_width - virus_surface.get_width()), random.randint(0, screen_height - virus_surface.get_height())))

    # Двигающийся текст
    moving_text = "TELERAM: KING VON"
    moving_font = pygame.font.SysFont("arial", 50)
    moving_text_surface = moving_font.render(moving_text, True, pygame.Color("red"))
    text_move_pos += 5
    if text_move_pos > screen_width:
        text_move_pos = -moving_text_surface.get_width()
    screen.blit(moving_text_surface, (text_move_pos, screen_height - 100))

    # Отображение .onion ссылок
    if show_onion_list:
        y_offset = 0
        for link in onion_list:
            onion_surface = pygame.font.SysFont("arial", 30).render(link, True, pygame.Color("green"))
            screen.blit(onion_surface, (random.randint(0, screen_width - onion_surface.get_width()), y_offset))
            y_offset += onion_surface.get_height() + 5

    # Показ изображения
    if show_image:
        screen.blit(image, ((screen_width - image.get_width()) // 2, (screen_height - image.get_height()) // 2))

    # Обновление экрана
    pygame.display.flip()
    frame_count += 1
    time.sleep(1 / clip.fps)

pygame.quit()
