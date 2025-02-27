from PIL import Image, ImageFilter
import random
import time


def blend_images(background_path, frontground_path, overlay_path, output_path):
    try:
        # Загружаем основное изображение и применяем эффект размытия
        background = Image.open(background_path)
        background = background.resize((1500, 1700), Image.LANCZOS)
        blurred_bg = background.filter(ImageFilter.GaussianBlur(5)) # Измените значение для более сильного/слабого размытия

        frontground = Image.open(frontground_path)
        blurred_fg = frontground.resize((1500, 1700), Image.LANCZOS)
        #blurred_fg = frontground.filter(ImageFilter.GaussianBlur(5))

        # Загружаем изображение для наложения и определяем его размеры
        overlay = Image.open(overlay_path)
        overlay = overlay.resize((900, 1500))
        overlay_width, overlay_height = overlay.size

        if overlay.mode != 'RGBA':
            overlay = overlay.convert('RGBA')
        opacity = random.uniform(0.6, 1.0)
        overlay = change_opacity(overlay, opacity)
        mask = overlay.split()[3]
        # Расчитываем позицию для наложения (по центру фона)
        bg_width, bg_height = blurred_bg.size
        position = ((bg_width - overlay_width) // 2, (bg_height - overlay_height) // 2)

        # Накладываем изображение поверх размытого фона
        blurred_bg.paste(overlay, position, mask)

        if blurred_fg.mode != 'RGBA':
            blurred_fg = blurred_fg.convert('RGBA')

        opacity = random.uniform(0.2, 0.3)
        blurred_fg = change_opacity(blurred_fg, opacity)
        mask = blurred_fg.split()[3]

        blurred_bg.paste(blurred_fg, (0, 0), mask)

        count_stickers = random.randint(30,40)
        random_sticker = random.randint(1, 609)

        for i in range(count_stickers):
            x = random.randint(1, 1500)
            y = random.randint(1, 1700)
            sticker = Image.open(f'stickers/{random_sticker}.png')
            sticker = sticker.resize((25, 25))
            if sticker.mode != 'RGBA':
                sticker = sticker.convert('RGBA')
            mask = sticker.split()[3]
            blurred_bg.paste(sticker, (x, y), mask)

        # Сохраняем результат в новый файл
        blurred_bg.save(output_path)
        print(f"Изображение успешно обработано и сохранено как {output_path}")
        time.sleep(1)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def change_opacity(image, opacity):
    # Загружаем исходное изображение

    # Создаем маску с новым уровнем непрозрачности
    mask = Image.new("L", image.size, int(255 * opacity))

    # Объединяем исходное изображение и маску
    image.putalpha(mask)

    # Сохраняем измененное изображение
    return image

print(1)