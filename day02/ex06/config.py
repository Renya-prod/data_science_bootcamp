import logging

BOT_TOKEN = "my_tokrn:lalalallala2I37tjWvaoieWyKWvYmwyHpIGxw"
CHAT_ID = "tutanumber"

logging.basicConfig(
    filename="analytics.log",
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
telegram_webhook_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
telegram_chat_id = f"{CHAT_ID}"

num_of_steps = 3

report_template = """
Report
We have made {total} observations from tossing a coin: {tails} of them were tails and {heads} of them were heads.
The probabilities are {tail_percent:.2f}% and {head_percent:.2f}%, respectively.
Our forecast is that in the next {steps} observations we will have: {predicted_tails} tail(s) and {predicted_heads} head(s).
"""