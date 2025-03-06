# Telegram Bot for Production Inventory Management

This project is a Telegram bot designed to automate the tracking of production and consumption of various materials in an industrial setting. The bot allows employees to record data about materials taken for production and products generated during manufacturing processes. All data is stored in a PostgreSQL database for further analysis and reporting.

## Key Features

- **Material Tracking**: Record data about materials taken for production (e.g., raw materials).
- **Product Tracking**: Record data about products generated during manufacturing processes.
- **Process Management**: Select processes (e.g., "Mill", "Dryer") and materials (e.g., "F4", "PPA", "Alcohol").
- **Data Confirmation**: Users can confirm the accuracy of entered data before saving it to the database.
- **Logging**: Log bot activities with the option to send logs to a Telegram chat.

## Technologies

- **Programming Language**: Python
- **Libraries**:
  - `aiogram` for Telegram API integration.
  - `psycopg2` for interacting with a PostgreSQL database.
  - `environs` for managing environment variables.
  - `logging` and `tglogging` for logging.
- **Database**: PostgreSQL

## Project Structure

- **`config.py`**: Bot settings, including menu commands, states, and keyboard buttons.
- **`handlers.py`**: Message and command handlers that manage user interaction logic.
- **`keyboard.py`**: Keyboards for user interaction.
- **`message.py`**: Class for database operations, including table creation and data insertion.
- **`program.py`**: Main script for running the bot and configuring logging.

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Gerrgor/storage_bot.git
   cd storage_bot
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
3. **Configure Environment Variables**:

   Create a .env file and add the following variables:
   ```bash
   BOT_TOKEN=your_bot_token
   db_host=your_database_host
   db_pass=your_database_password
   log_chat_id=your_log_chat_id
4. **Run the Bot:**
    ```bash
    python program.py

## Usage Example

1. Start the bot using the /start command.
2. Select a process (e.g., "Mill" or "Dryer").
3. Choose the type of data (e.g., "Taken" or "Accumulated").
4. Select a material and enter the quantity.
5. Confirm the accuracy of the entered data.
