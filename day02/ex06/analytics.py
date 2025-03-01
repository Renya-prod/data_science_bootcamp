import os
import logging
import requests
from random import randint
import config


class Research:
    def __init__(self, file_path):
        logging.info("Initializing Research class")
        if not os.path.isfile(file_path):
            logging.error(f"The file '{file_path}' does not exist.")
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        self.file_path = file_path

    def file_reader(self, has_header=True):
        logging.info("Reading file")
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
        except Exception as e:
            logging.error(f"Error reading the file: {e}")
            raise RuntimeError(f"Error reading the file: {e}")

        if len(lines) < 1:
            logging.error("File must contain at least one line of data.")
            raise ValueError("File must contain at least one line of data.")

        if has_header:
            header = lines[0].strip()
            if ',' not in header or len(header.split(',')) != 2:
                logging.error("Invalid header format")
                raise ValueError("Header must contain exactly two strings delimited by a comma.")
            lines = lines[1:]

        data = []
        for line in lines:
            line = line.strip()
            if line not in {"0,1", "1,0"}:
                logging.error(f"Invalid data row: {line}")
                raise ValueError("Each data line must be either '0,1' or '1,0'.")
            data.append(list(map(int, line.split(','))))

        logging.info("File reading completed successfully")
        return data

    def send_telegram_message(self, message):
        logging.info("Sending Telegram message")
        try:
            payload = {
                "chat_id": config.telegram_chat_id,
                "text": message,
            }
            response = requests.post(config.telegram_webhook_url, json=payload)
            if response.status_code == 200:
                logging.info("Telegram message sent successfully")
            else:
                logging.error(f"Failed to send Telegram message: {response.status_code}, {response.text}")
        except Exception as e:
            logging.error(f"Error sending Telegram message: {e}")

    class Calculations:
        def __init__(self, data):
            logging.info("Initializing Calculations class")
            self.data = data

        def counts(self):
            logging.info("Calculating the counts of heads and tails")
            heads = sum(row[0] for row in self.data)
            tails = sum(row[1] for row in self.data)
            logging.info(f"Counts calculated: heads={heads}, tails={tails}")
            return heads, tails

        def fractions(self, heads, tails):
            logging.info("Calculating fractions")
            total = heads + tails
            if total == 0:
                logging.warning("Total count is zero, returning 0 fractions")
                return 0, 0
            head_percent = (heads / total) * 100
            tail_percent = (tails / total) * 100
            logging.info(f"Fractions calculated: heads={head_percent:.2f}%, tails={tail_percent:.2f}%")
            return head_percent, tail_percent

    class Analytics(Calculations):
        def predict_random(self, steps):
            logging.info(f"Generating {steps} random predictions")
            predictions = [[randint(0, 1), 1 - randint(0, 1)] for _ in range(steps)]
            logging.info(f"Random predictions generated: {predictions}")
            return predictions

        def predict_last(self):
            logging.info("Getting the last observation")
            if not self.data:
                logging.error("No data available to predict the last observation.")
                raise ValueError("No data available to predict the last observation.")
            last_observation = self.data[-1]
            logging.info(f"Last observation: {last_observation}")
            return last_observation

        def save_file(self, data, file_name, extension='txt'):
            file_path = f"{file_name}.{extension}"
            logging.info(f"Saving file: {file_path}")
            try:
                with open(file_path, 'w') as file:
                    file.write(data)
                logging.info(f"File saved successfully: {file_path}")
            except Exception as e:
                logging.error(f"Error saving file: {e}")
                raise RuntimeError(f"Error saving file: {e}")
