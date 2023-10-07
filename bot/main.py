import telebot
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot_token = '6512530190:AAEvpDhhmldt12QbV5ZVSook7g0f7UmLU4o'
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=["challenge"])
def challenge_handler(message):
    user_args = message.text.split()[1:]
    if len(user_args) != 2:
        bot.send_message(message.chat.id, "Uso incorrecto. Usa /challenge @opponent stake")
        return

    opponent, stake = user_args
    challenger = message.from_user.username

    try:
        # Llamar al endpoint para crear una nueva sala
        response = requests.post('http://localhost:3000/create-room', json={
            'challenger': challenger,
            'opponent': opponent,
            'stake': stake,
            'type': 'private'
        })

        if response.status_code == 200:
            data = response.json()
            room_id = data['roomId']
            room_link = data['roomLink']  # Aquí obtenemos el enlace de la sala
            markup = InlineKeyboardMarkup(row_width=2)
            accept_button = InlineKeyboardButton("Accept", callback_data=f'accept:{room_id}')
            cancel_button = InlineKeyboardButton("Cancel", callback_data=f'cancel:{room_id}')
            markup.add(accept_button, cancel_button)
            bot.send_message(message.chat.id, f"@{challenger} ha retado a @{opponent} por {stake}", reply_markup=markup)
            # Agregar mensaje de registro
            print(f"Sala creada con ID: {room_id}")
            bot.send_message(message.chat.id, f"Enlace de la sala: {room_link}") 
        else:
            bot.send_message(message.chat.id, "Algo salió mal al crear la sala.")
            # Agregar mensaje de registro en caso de error HTTP
            print(f"Error HTTP al crear la sala. Código de estado: {response.status_code}")
    
    except Exception as e:
        # Capturar excepciones y mostrar el mensaje de error en la consola
        print(f"Error al crear la sala: {str(e)}")

# Resto del código del bot...

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    action, room_id = call.data.split(":")
    if action == 'accept':
        game_room_url = f"http://localhost:3000/room/{room_id}"  # URL de la sala de juego
        bot.answer_callback_query(call.id, f"Has aceptado el reto. Ve a la sala {game_room_url}.")
    elif action == 'cancel':
        bot.edit_message_text("Reto cancelado.", call.message.chat.id, call.message.message_id)

if __name__ == "__main__":
    print("Bot initialized")
    bot.polling()
