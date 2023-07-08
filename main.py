import random
from flask import Flask, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

message_file = os.path.join(os.getcwd(), 'messages.txt')


@app.route('/post/message', methods=['POST'])
def save_message():
    data = request.get_json()
    message = data["message"]
    with open(message_file, 'at') as new_message:
        new_message.write(str(message+'\n'))
        new_message.flush()

    return 'Message Writen in file'


@app.route('/get/all-messages', methods=['GET'])
def get_messages():
    return_messages = ''
    all_messages = open(message_file, 'rt')
    for message in all_messages:
        return_messages += message
    all_messages.close()
    return return_messages


@app.route('/get/random-message')
def get_random_message():
    all_messages = open(message_file).read()
    messages = all_messages.split('\n')
    return random.choice(messages)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
