import streamlit as st
from rag_chatbot_psa import RAGChatbot
import logging

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logging.info(" I AM HERE 1")

# Initialize the chatbot and store it in session state if it doesn't already exist
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = RAGChatbot()
    logging.info("Chatbot initialized and stored in session state")

chatbot = st.session_state.chatbot

# App title and description
st.title("💬 Chatbot - Ask your questions away")
st.write(
    """
    RAG based chatbot that uses a custom generative model to answer your queries.
    """
)

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

logging.info(" I AM HERE 2")

# Add a dropdown menu for selecting response type
response_type = st.selectbox("Choose response type:", ("Fetch top 3 relevant documents", "Extract answer"))

if response_type:
    logging.info("response type : " + response_type)
else:
    logging.info("response type : None")

# Chat input field
prompt = st.chat_input("What is up?")

if prompt:
    logging.info(" I AM HERE 3")
    logging.info("prompt : " + prompt)

    # Store and display the user's prompt
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    logging.info(" I AM HERE 4")

    if response_type == "Fetch top 3 relevant documents":
        logging.info(" I AM HERE 5")
        scores, retrieved_documents = chatbot.search(prompt, 3)
        retrieved_documents2 = [doc["text"] for doc in retrieved_documents["text"]]

        response = "Here are some relevant documents:\n"
        for idx, doc in enumerate(retrieved_documents2):
            response += "\n--------------------------"
            response += f"\n**Document {idx+1}:**\n<div style='font-size:14px;'>{doc}</div>"
        response = response.replace('\n', '<br>')  # Replace newlines with HTML breaks
    else:
        logging.info(" I AM HERE 6")
        # Generate a response using the custom generative model
        response = chatbot.rag_chatbot(prompt, k=5, response_type=response_type)

    logging.info(" I AM HERE 7")

    # Store and display the bot's response
    st.session_state.messages.append({"role": "bot", "content": response})
    with st.chat_message("bot"):
        st.markdown(response, unsafe_allow_html=True)

    logging.info(" I AM HERE 8")

else:
    logging.info("Prompt : None")
