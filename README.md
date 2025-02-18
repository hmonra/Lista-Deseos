# 🛒 Bot de Seguimiento de Lista de deseos preconfigurada

Este script de Python utiliza Selenium y Undetected ChromeDriver para monitorear una lista de deseos de PcComponentes y notificar a través de Telegram cuando un artículo se añade a la cesta.  ¡Ideal para no perderte esa oferta que tanto esperabas!

## 🚀 Características

*   **Monitoreo Continuo:**  El script revisa periódicamente la lista de deseos en busca de cambios.
*   **Notificaciones de Telegram:** Recibe alertas instantáneas en tu móvil cuando un artículo se añade a la cesta.  Incluye enlace a la lista de deseos, al artículo y al resumen de la cesta.
*   **Detección de Captcha:**  Integra solución automática de captchas para evitar interrupciones.
*   **Manejo de Errores:**  Incluye gestión de errores como Timeouts y "Bad Gateway", con reintentos automáticos y notificaciones por Telegram.
*   **Aceptación automática de Cookies:** El script acepta las cookies para que no tengas que hacerlo manualmente.
*   **Fácil de usar:** Configuración sencilla mediante variables de entorno o directamente en el código (aunque se recomienda usar variables de entorno).

## ⚙️ Instalación

1.  **Requisitos:**
    *   Python 3.x
    *   Las bibliotecas especificadas en `requirements.txt` (instalar con `pip install -r requirements.txt`).  Puedes crear este archivo con `pip freeze > requirements.txt` después de instalar las librerías.
    *   Undetected ChromeDriver (incluido en el repositorio).
    *   Cuenta de Telegram y Bot creado (obtén el token y el chat ID).

2.  **Clonado del repositorio:**

    ```bash
    git clone https://github.com/hmonra/Lista-Deseos.git
    ```

3.  **Instalación de dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuración:**

    *   **Variables de entorno (Recomendado):**
        Crea variables de entorno para `TOKEN_BOT` y `CHAT_ID` con los valores de tu bot de Telegram.
        Ejemplo en Linux/macOS:
        ```bash
        export TOKEN_BOT="TU_TOKEN_AQUI"
        export CHAT_ID="TU_CHAT_ID_AQUI"
        ```
        Ejemplo en Windows:
        ```bash
        set TOKEN_BOT="TU_TOKEN_AQUI"
        set CHAT_ID="TU_CHAT_ID_AQUI"
        ```
    *   **Directamente en el código (No recomendado):**
        Edita el script `main.py` y reemplaza los valores de `bot_token` y `bot_chatid` con los de tu bot de Telegram.
    *   Modifica la variable `lista_deseos` con la URL de tu lista de deseos de PcComponentes.

## 🚀 Uso

Ejecuta el script:

```bash
python main.py