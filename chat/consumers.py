from channels.generic.websocket import AsyncWebsocketConsumer
import json
import logging

class ChatConsumer(AsyncWebsocketConsumer):
    logger = logging.getLogger(__name__)

    async def connect(self):
        self.logger.info("WebSocket connection established.")
        await self.accept()

    async def disconnect(self, close_code):
        self.logger.info("WebSocket connection closed.")

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json['message']

            # Enviar mensagem para o WebSocket
            await self.send(text_data=json.dumps({
                'message': message
            }))
        except json.JSONDecodeError:
            self.logger.error("Invalid JSON received.")
        except Exception as e:
            self.logger.error(f"Error processing message: {e}")
