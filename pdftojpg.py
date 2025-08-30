import pyautogui
import time

# Koordinatalar
coord1 = (874, 330)
coord2 = (1678, 979)
coord3 = (859, 272)
coord4 = (730, 285)

# Massivlar
list1 = [
    "Nasullayev.pdf",
    "Ibrohimova Madina.pdf",
    "Qudratullayev.pdf",
    "Xayrullayev.pdf",
]

with open("log.txt", "w", encoding="utf-8") as log_file:
    for word in list1:
        # 1-koordinataga borib bosish
        pyautogui.moveTo(coord1[0], coord1[1], duration=0.5)
        pyautogui.click()
        log_file.write(f"1-koordinataga bosildi ({coord1[0]}, {coord1[1]})\n")
        print(f"1-koordinataga bosildi ({coord1[0]}, {coord1[1]})")
        time.sleep(1)

        # So'zni yozish va Enter bosish
        pyautogui.write(word, interval=0.1)
        pyautogui.press('enter')
        log_file.write(f"So'z yozildi va Enter bosildi: {word}\n")
        print(f"So'z yozildi va Enter bosildi: {word}")
        time.sleep(2)

        # 2-koordinataga borib bosish
        pyautogui.moveTo(coord2[0], coord2[1], duration=0.5)
        pyautogui.click()
        log_file.write(f"2-koordinataga bosildi ({coord2[0]}, {coord2[1]})\n")
        print(f"2-koordinataga bosildi ({coord2[0]}, {coord2[1]})")
        time.sleep(1)

        # 3-koordinataga borib bosish
        pyautogui.moveTo(coord3[0], coord3[1], duration=0.5)
        pyautogui.click()
        log_file.write(f"3-koordinataga bosildi ({coord3[0]}, {coord3[1]})\n")
        print(f"3-koordinataga bosildi ({coord3[0]}, {coord3[1]})")
        time.sleep(1)

        # 4-koordinataga borib bosish
        pyautogui.moveTo(coord4[0], coord4[1], duration=0.5)
        pyautogui.click()
        log_file.write(f"4-koordinataga bosildi ({coord4[0]}, {coord4[1]})\n")
        print(f"4-koordinataga bosildi ({coord4[0]}, {coord4[1]})")
        time.sleep(2)

        # Yakuniy log yozish
        log_file.write(f"Jarayon muvaffaqiyatli yakunlandi: {word}\n\n")
        print(f"Jarayon muvaffaqiyatli yakunlandi: {word}\n")

print("Barcha jarayonlar yakunlandi!")