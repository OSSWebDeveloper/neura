import pyautogui
import time

# Koordinatalar
coord1 = (586, 320)
coord2 = (564, 370)
coord3 = (560, 447)

# Massivlar
list2 = [
    "Nasullayev.pdf",
    "Ibrohimova Madina.pdf",
    "Qudratullayev.pdf",
    "Xayrullayev.pdf",
]

list1 = [
    # "Djuraeva Nodira_page-0001.jpg",
    "Nasullayev_page-0001.jpg",
    "Ibrohimova Madina_page-0001.jpg",
    "Qudratullayev_page-0001.jpg",
    "Xayrullayev_page-0001.jpg",
]


# Log fayl ochamiz
with open("log.txt", "w", encoding="utf-8") as log_file:
    for i in range(len(list1)):
        jpg_file = list1[i]
        pdf_file = list2[i]

        # 1-koordinataga borib bosish
        pyautogui.moveTo(coord1[0], coord1[1], duration=0.5)
        pyautogui.click()
        time.sleep(1)

        # list1[i] ni yozish va Enter bosish
        pyautogui.write(jpg_file, interval=0.1)
        pyautogui.press('enter')
        time.sleep(2)

        # 2-koordinataga borib bosish
        pyautogui.moveTo(coord2[0], coord2[1], duration=0.5)
        pyautogui.click()
        time.sleep(1)

        # list2[i] ni yozish va Enter bosish
        pyautogui.write(pdf_file, interval=0.1)
        pyautogui.press('enter')
        time.sleep(2)

        # 3-koordinataga borib bosish
        pyautogui.moveTo(coord3[0], coord3[1], duration=0.5)
        pyautogui.click()
        time.sleep(5)

        # Log yozish
        log_file.write(f"{jpg_file} ↔ {pdf_file} moslashtirildi\n")
        print(f"{jpg_file} ↔ {pdf_file} moslashtirildi")

print("Jarayon tugadi!")
