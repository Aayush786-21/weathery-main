import asyncio
import os
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from barsha import get_weather

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your weather bot. Send me the name of a city to get the weather.')

# Function to handle weather requests
async def handle_weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = ' '.join(context.args) if context.args else 'Kathmandu'  # Default city if none provided
    weather_description, temperature = get_weather(city)
    
    if weather_description and temperature is not None:
        response = f"The weather in {city} is {weather_description} with a temperature of {temperature}°C."
    else:
        response = "Sorry, I couldn't fetch the weather information. Please check the city name."

    await update.message.reply_text(response)

# Load the bot token from environment variables
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')

async def main():
    # Use the loaded token instead of the hardcoded string
    app = ApplicationBuilder().token(bot_token).build()
    
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_weather))

    await app.initialize()
    await app.run_polling()

# Apply nest_asyncio to allow running within Jupyter or other environments
nest_asyncio.apply()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if "This event loop is already running" in str(e):
            # If the event loop is already running, we should use a task to run our main function
            asyncio.get_event_loop().create_task(main())
        else:
            raise
