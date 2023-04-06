# WhatsApp Chatbot using OpenAI and Twilio

This project is a WhatsApp chatbot created using OpenAI's text and image generation API and Twilio's messaging API. It is designed to respond to user messages with generated text or images based on the content of the message. The chatbot can also understand and respond to messages in Hindi.

## Features

- Generates text based on user prompts using OpenAI's text generation API
- Generates images based on user prompts using OpenAI's image generation API
- Responds to messages in Hindi as well as English

## Getting Started

To use this chatbot, you will need to set up a Twilio account and a WhatsApp Sandbox,ngrok, as well as an OpenAI API key. You will also need to install the required Python packages listed in `requirements.txt`.

Once you have set up your Twilio and OpenAI accounts and installed the required packages, you can run the chatbot using the following command:

```bash
python app.py
```

## Usage
To use the chatbot, simply send a message to the WhatsApp number associated with your Twilio Sandbox. If your message contains the word "IMAGE", the chatbot will generate an image based on the content of your message. If your message contains any other text, the chatbot will generate a response based on the content of your message.


To use this code, you will need to follow these steps:

### 1. The this repository to your local machine:
```bash
git clone https://github.com/example/whatsapp-chatbot.git
```
### 2. Navigate to the project directory:
```bash
cd whatsapp-chatbot
```
### 3. Install the required packages:
```bash
pip install -r requirements.txt
```
### 4. Put your OpenAI API Key 
Set your OpenAI API key by replacing <OPEN AI KEY> with your own API key in the openai.api_key variable in the code.

### 5. Connect your local server to the internet using ngrok.
Download and install ngrok, then run it with the following command:

```bash
ngrok http 4000
```
This will create a public URL for your local server. Make note of the URL, as you will need it for the next step.

### 6. Create a webhook URL for your Twilio account.
Log in to your Twilio account and navigate to the "Messaging" section. Under "WhatsApp Sandbox", enter the ngrok URL followed by "/WhatsappChatBot" as the webhook URL. For example, if your ngrok URL is https://XYZ.ngrok.io, your webhook URL would be https://XYZ.ngrok.io/WhatsappChatBot.

### 7. Run the server:

```bash
python app.py
```

### 8. Start a WhatsApp conversation with your Twilio number and send a message to test the chatbot.

`Note: You will need to keep the server running while you are using the chatbot. If you make changes to the code, you will need to stop and restart the server for the changes to take effect.`


## Contributors
- Kanak Poddar

## License
This project is licensed under the MIT License.
