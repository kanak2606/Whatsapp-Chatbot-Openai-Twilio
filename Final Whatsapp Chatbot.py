import openai
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# Set the OpenAI API key
openai.api_key = "<OPEN AI KEY>"

# Initialize the Flask app
app = Flask(__name__)

# Maintain conversation history as a global variable
Conversation_memory = []
# Handle incoming messages from the WhatsApp bot (Remember to add the endpoint in Twilio)
@app.route('/WhatsappChatBot', methods=['POST'])
def bot():
    msg_from_user = request.values.get('Body', '').lower()
    Server_resp = MessagingResponse()
    msg = Server_resp.message()

    # Handle incoming messages from the WhatsApp bot (Remember to add the endpoint in Twilio)
    if 'image' in msg_from_user:
        # Generate and send an image related to the incoming message
        msg.media(Dall(msg_from_user))
        print(msg_from_user)
        return str(Server_resp)
    # Check if the incoming message is a greeting message
    elif 'hi' in msg_from_user and len(msg_from_user.strip().split()) == 1:
        # Send an introductory message to the user
        msg.body("Hello I am a whatsapp Chatbot Created by Kanak Poddar \n"
                 "Here is the list of Tasks of i can perform \n"
                 "I can Generate any text and give answer to all your queries \n"
                 "If Any message Contain the word IMAGE, I will generate an image related to it \n"
                 )
        print(msg_from_user)
        return str(Server_resp)
    else:
        # If the incoming message is not a greeting or an image request, generate a response using OpenAI
        msg.body(AI(msg_from_user))
        print(msg_from_user)
        print(AI(msg_from_user))
        return str(Server_resp)

# Function to generate a response using OpenAI
def AI(msg_from_user):
    prompt = msg_from_user
    bot_response = generate_response(prompt)
    return bot_response

# Function to generate a response using OpenAI's Text=Davinci-003
def generate_response(prompt):
    global Conversation_memory

    # Combine the prompt with the conversation history
    full_prompt = '\n'.join(Conversation_memory + [prompt])
    # Generate a response from OpenAI
    bot_response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=full_prompt,
        temperature=0.2,
        max_tokens=2048,
        n=1,
        stop=None,
        timeout=10,
    )
    # Get the response text from OpenAI
    message = bot_response.choices[0].text.strip()

    # Add the current prompt and response to the conversation history
    Conversation_memory.append(prompt)
    Conversation_memory.append(message)

    return message

# Generate an image using OpenAI's DALL-E API
def Dall(msg_from_user):
    PROMPT = msg_from_user
    bot_response = openai.Image.create(
        prompt=PROMPT,
        n=1,
        size="256x256",
    )
    return (bot_response["data"][0]["url"])


if __name__ == '__main__':
    # Run the Flask app on port 4000
    app.run(port=4000)
