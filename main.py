# Librerias
import time
import undetected_chromedriver.v2 as uc
import telebot
from datetime import datetime
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Opciones de navegación
options = uc.ChromeOptions()
options.page_load_strategy = 'normal'
options.add_argument('--start')
options.add_argument('--disable-extensions')
options.add_argument("--disable-software-rasterizer")
options.add_argument('--ignore-ssl-errors')
options.add_argument('--allow-insecure-localhost')
options.add_argument('--disable-gpu')
options.add_argument("--disable-infobars")
options.add_argument("--force-device-scale-factor=1")
options.add_argument("--ignore-ssl-errors")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--disable-notifications')
options.add_argument("--mute-audio")
options.add_argument("--disable-hang-monitor")
# options.add_argument('--blink-settings=imagesEnabled=false')
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")
options.add_argument(
    "user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36')
driver = uc.Chrome(options=options)
# driver.maximize_window()

# HORA INICIO SCRIPT
hora_inicial = datetime.now()

lista_deseos = 'TU_LISTA_DE_DESEOS' # AÑADIMOS ENLACE A LA LISTA DE DESEOS DE PCCOMPONENTES

# BOT TELEGRAM ERROR TIME OUT
def telegram_bot_sendtext4():
    bot_token = 'TOKEN_BOT' # AÑADIMOS TOKEN DEL BOT
    bot_chatid = 'CHAT_ID' # AÑADIMOS ID DEL CHAT
    combo_producto = '<b>❌ BOT CESTA - Error en url, time out ❌</b>' + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
# BOT TELEGRAM CAPTCHA DETECTADO, BOTÓN PULSADO
def telegram_bot_sendtext6():
    bot_token = 'TOKEN_BOT' # AÑADIMOS TOKEN DEL BOT
    bot_chatid = 'CHAT_ID' # AÑADIMOS ID DEL CHAT
    combo_producto = '<b>✅ BOT CESTA - Captcha detectado, pulsando botón ✅️</b>' + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
# BOT TELEGRAM ERROR AL PULSAR CAPTCHA
def telegram_bot_sendtext7():
    bot_token = 'TOKEN_BOT' # AÑADIMOS TOKEN DEL BOT
    bot_chatid = 'CHAT_ID' # AÑADIMOS ID DEL CHAT
    combo_producto = '<b>⛔️ BOT CESTA - Captcha detectado, fallo al pulsar botón ⛔️</b>' + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
# BOT TELEGRAM ERROR BAD GATEWAY
def telegram_bot_sendtext8():
    bbot_token = 'TOKEN_BOT' # AÑADIMOS TOKEN DEL BOT
    bot_chatid = 'CHAT_ID' # AÑADIMOS ID DEL CHAT
    combo_producto = '<b>☑️ BOT CESTA - Bad gateway, refresco página ☑️</b>' + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")
# BOT AVISO CESTA CON ARTICULO
def telegram_bot_sendtext9():
    enlace_summary = "https://www.pccomponentes.com/cart/summary"
    bot_token = 'TOKEN_BOT' # AÑADIMOS TOKEN DEL BOT
    bot_chatid = 'CHAT_ID' # AÑADIMOS ID DEL CHAT
    combo_producto = '<b>💎 Artículo encontrado 💎</b>' + '\n' + '\n'
    combo_producto += '<b>' + lista_deseos + '</b>' + '\n' + '\n'
    combo_producto += '<b>' + enlace + '</b>' + '\n' + '\n'
    combo_producto += '<b>' + enlace_summary + '</b>' + '\n'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(bot_chatid, combo_producto, parse_mode="html")


while True:
    try:
        driver.get(lista_deseos)
        print("*** Script corriendo desde:", hora_inicial, "***")
        print("Accediendo al enlace lista deseos..")
    except TimeoutException:
        print("")
        print("Url Time out..")
        print("Volviendo a escanear...")
        print("")
        telegram_bot_sendtext4()
        continue
    try:
        if driver.find_elements(By.CLASS_NAME, 'inline-block'):
            print("Bad gateway..")
            print("Volviendo a escanear...")
            telegram_bot_sendtext8()
            continue
        if driver.find_elements(By.ID, 'challenge-running'):
            print("Detectado por captcha..")
            time.sleep(3)
            WebDriverWait(driver, 40) \
                .until(EC.visibility_of_element_located and EC.element_to_be_clickable(
                (By.CLASS_NAME, 'hcaptcha-box'))).click()
            print("Pulso botón captcha..")
            telegram_bot_sendtext6()
            time.sleep(3)
        else:
            print("Bypass captcha OK..")
            if driver.find_elements(By.CLASS_NAME, 'btn.btn-block.btn-primary.btn-lg.m-t-1.accept-cookie'):
                print("Cookies pendientes de aceptar..")
                WebDriverWait(driver, 40) \
                    .until(EC.visibility_of_element_located and EC.element_to_be_clickable(
                    (By.CLASS_NAME, 'btn.btn-block.btn-primary.btn-lg.m-t-1.accept-cookie'))).click()
                print("Cookies aceptadas..")
                time.sleep(2)
            else:
                print("Cookies OK..")
            print("Se comprueba cantidad de articulos en la cesta..")
            cesta_vacia = WebDriverWait(driver, 40) \
                .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.ID, 'root')))
            cesta_vacia = cesta_vacia.text
            # print(cesta_vacia)
            if "Tu cesta está vacía" not in cesta_vacia:
                print("Detectado artículo en la cesta, mando aviso..")
                elements = driver.find_elements(By.CLASS_NAME, 'sc-gJLAYP')
                try:
                    for e in elements:
                        enlace = (e.get_attribute('href'))
                        print(enlace)
                        telegram_bot_sendtext9()
                except TimeoutException:
                    print("")
                    print("Url Time out..")
                    print("Volviendo a escanear...")
                    print("")
                    telegram_bot_sendtext7()
                    continue
            else:
                current_time = datetime.now().time()
                print("Hora última consulta: ", current_time)
                print("Nada en la cesta, sigo escaneando..")
    except TimeoutException:
        print("")
        print("Url Time out..")
        print("Volviendo a escanear...")
        print("")
        telegram_bot_sendtext7()
        continue
