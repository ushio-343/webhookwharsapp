from fastapi import FastAPI
import requests
import json

app = FastAPI()

# Tu token de autenticación (asegúrate de reemplazarlo)
AUTH_TOKEN = "EAAYbJsPcZAXYBO9ui61bJUP0IhIeZBbW8IoTPpFYyxgejbEXm72wfu8JIwkJSbBJAUr5lZC1XZBLul7ZBo6MZA2Ihh1U6i8ZBjkUisZAgpiiMeeY8CXZASGHkL3ANZBsmrPdZBAZAda0xceJZBBMPrNRODtqMUGad322E8XyoKUDdl5qrNZBVfZA3ikerOKQPviXn5reNS753RA40aRlIZCNt3kjZCXZBMZCWwoXWEZD"
# URL de la API de WhatsApp
WHATSAPP_API_URL = "https://graph.facebook.com/v20.0/470243629495943/messages"

# Endpoint para enviar mensajes de WhatsApp
@app.post("/send-message/")
async def send_whatsapp_message():
    # Cuerpo de la solicitud (el JSON con los detalles del mensaje)
    payload = {
        "messaging_product": "whatsapp",
        "to": "529512198832",  # Número del destinatario
        "type": "template",
        "template": {
            "name": "hello_world",
            "language": {
                "code": "en_US"
            }
        }
    }

    # Encabezados
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }

    # Enviar la solicitud POST
    response = requests.post(WHATSAPP_API_URL, headers=headers, data=json.dumps(payload))

    # Verificar si el mensaje fue enviado con éxito
    if response.status_code == 200:
        return {"status": "success", "message": "Mensaje enviado"}
    else:
        return {
            "status": "error",
            "code": response.status_code,
            "details": response.text
        }
