def show_messages(messages):
    print("\nList of messages: ")
    for message in messages:
        print(message)
def send_messages(messages, sent_messages):
    while messages:
        sent = messages.pop()
        sent_messages.append(sent)
    
user_messages = ['Hello', 'LOL', 'OMW', 'ASAP', 'OMG', 'WTF???!!!']
user_sent_messages = []
show_messages(user_messages)
send_messages(user_messages, user_sent_messages)
show_messages(user_messages)
show_messages(user_sent_messages)