import sys
from analytics import Research
import config
import logging

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 make_report.py file")
        sys.exit(1)

    file_path = sys.argv[1]
    research = None

    try:
        research = Research(file_path)
        data = research.file_reader()

        analytics = Research.Analytics(data)
        heads, tails = analytics.counts()
        head_percent, tail_percent = analytics.fractions(heads, tails)

        predictions = analytics.predict_random(config.num_of_steps)
        predicted_heads = sum(pred[0] for pred in predictions)
        predicted_tails = sum(pred[1] for pred in predictions)

        report = config.report_template.format(
            total=len(data),
            tails=tails,
            heads=heads,
            tail_percent=tail_percent,
            head_percent=head_percent,
            steps=config.num_of_steps,
            predicted_tails=predicted_tails,
            predicted_heads=predicted_heads
        )

        analytics.save_file(report, "report", "txt")
        research.send_telegram_message('The report has been successfully created')

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        try:
            if research is None:
                import requests
                payload = {
                    "chat_id": config.telegram_chat_id,
                    "text": f"An error occurred: {e}"
                }
                response = requests.post(config.telegram_webhook_url, json=payload)
                if response.status_code == 200:
                    print("Telegram notification sent.")
                else:
                    print(f"Failed to send Telegram message: {response.status_code}, {response.text}")
            else:
                research.send_telegram_message(f"The report hasn’t been created due to an error: {e}")
        except Exception as telegram_error:
            logging.error(f"Failed to send Telegram message: {telegram_error}")
            print(f"Error: Failed to send Telegram message: {telegram_error}")
