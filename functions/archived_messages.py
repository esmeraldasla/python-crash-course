"""The purpose of this program is to show that the original list has retained its messages."""

def show_messages(messages):
    "Print all the messages in the list"
    print("Showing all messages")
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    print("\n Sending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


messages = ['Hello there!', 'How are you?', 'Bye bye!']
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)

