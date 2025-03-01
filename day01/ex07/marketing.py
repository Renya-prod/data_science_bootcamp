def call_center(clients, recipients):
    clients_set = set(clients)
    recipients_set = set(recipients)
    return list(clients_set - recipients_set)

def potential_clients(clients, participants):
    clients_set = set(clients)
    participants_set = set(participants)
    return list(participants_set - clients_set)

def loyalty_program(clients, participants):
    clients_set = set(clients)
    participants_set = set(participants)
    return list(clients_set - participants_set)

def main(task):
    clients = [
        'andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
        'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
        'elon@paypal.com', 'jessica@gmail.com'
    ]
    participants = [
        'walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org',
        'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org',
        'mr@robot.gov', 'eleven@yahoo.com'
    ]
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    if task == "call_center":
        result = call_center(clients, recipients)
    elif task == "potential_clients":
        result = potential_clients(clients, participants)
    elif task == "loyalty_program":
        result = loyalty_program(clients, participants)
    else:
        raise ValueError("Invalid task name")

    for email in result:
        print(email)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Error, you should use: python3 marketing.py <task_name>")
    else:
        main(sys.argv[1])
