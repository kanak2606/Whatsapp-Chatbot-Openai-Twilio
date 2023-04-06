# WhatsApp Chatbot using OpenAI and Twilio

This project is a WhatsApp chatbot created using OpenAI's text and image generation API and Twilio's messaging API. It is designed to respond to user messages with generated text or images based on the content of the message. The chatbot can also understand and respond to messages in Hindi.

## Features

- Generates text based on user prompts using OpenAI's text generation API
- Generates images based on user prompts using OpenAI's image generation API
- Responds to messages in Hindi as well as English

## Getting Started

To use this chatbot, you will need to set up a Twilio account and a WhatsApp Sandbox, as well as an OpenAI API key. You will also need to install the required Python packages listed in `requirements.txt`.

Once you have set up your Twilio and OpenAI accounts and installed the required packages, you can run the chatbot using the following command:

```bash
python app.py
## Usage
To use the chatbot, simply send a message to the WhatsApp number associated with your Twilio Sandbox. If your message contains the word "IMAGE", the chatbot will generate an image based on the content of your message. If your message contains any other text, the chatbot will generate a response based on the content of your message.

## Contributors
- Kanak Poddar

## License
This project is licensed under the MIT License.
