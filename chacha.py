import openai
import gradio as gr

openai.api_key = "Your Api Key here"

messages = [{
    "role": "system",
    "content": "You are Chacha Chaudhary, a wise and witty travel guide; You help users by Namami Gange initiative, promoting river conservation and cultural heritage"
}]

def custom_chatgpt(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    chatgpt_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": chatgpt_reply})
    return chatgpt_reply

avatar_url = "https://cdn.imweb.me/upload/S20211026228188315d8e6/5ec40eea82b4d.jpg"  

with gr.Blocks() as demo:
    gr.Markdown("<h1 align='center'>Chatbot for Travel Assistant</h1>")
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Image(avatar_url, label="Chacha Chaudhary Avatar", show_label=False)
        with gr.Column(scale=3):
            chatbot = gr.Chatbot()
            msg = gr.Textbox(
                label="You:", placeholder="Type your message here..."
            )
            send = gr.Button("Send")
    
    def respond(message, chat_history):
        bot_response = custom_chatgpt(message)
        chat_history.append((message, bot_response))
        return "", chat_history

    send.click(respond, inputs=[msg, chatbot], outputs=[msg, chatbot])
    msg.submit(respond, inputs=[msg, chatbot], outputs=[msg, chatbot])

demo.launch(share=True)
