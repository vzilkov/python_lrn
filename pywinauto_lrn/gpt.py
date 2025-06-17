import sys
import os
import time
from gpt4all import GPT4All #, get_model_list
import logging

# --- 0. Basic Configuration and Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- 1. Choose Your Model ---
# You can find available model names on the GPT4All website:
# https://gpt4all.io/index.html
# Or use get_model_list() to see what's available programmatically (see section 7).

# Recommended models for good balance of performance and quality:
# - mistral-7b-openorca.Q4_0.gguf
# - nomic-llama-2-7b-chat.Q4_0.gguf
# - nous-hermes-llama2-13b.Q4_0.gguf (requires more RAM)

# For this example, let's use a popular and relatively small model:
MODEL_NAME = "mistral-7b-openorca.Q4_0.gguf"

# Optional: Specify a custom directory for models.
# If not specified, models will be downloaded to ~/.cache/gpt4all/ (Linux/macOS)
# or C:\Users\<YourUser>\AppData\Local\nomic.ai\GPT4All\ (Windows)
# MODEL_DIR = "./gpt4all_models/"
# os.makedirs(MODEL_DIR, exist_ok=True) # Ensure the directory exists

# --- 2. Initialize and Load the Model ---
# The GPT4All constructor will automatically download the model
# if it's not found in the specified (or default) directory.
# This step can take a while the first time you run it for a new model.
logger.info(f"Attempting to load model: {MODEL_NAME}")

# model = None # Initialize outside try-except
def init():
    try:
        # If using a custom directory:
        # model = GPT4All(MODEL_NAME, model_path=MODEL_DIR, allow_download=True)
        
        # Using default path and allowing download (most common):
        model = GPT4All(MODEL_NAME, allow_download=True)
        logger.info(f"Model '{MODEL_NAME}' loaded successfully!")
        logger.info(f"Model path: {model.model.model_path}") # Access the underlying model object
    except Exception as e:
        logger.error(f"Failed to load or download model '{MODEL_NAME}': {e}")
        logger.error("Please check if the model name is correct, you have internet connection for initial download, and sufficient disk space.")
        sys.exit(1) # Exit if we can't load the model

    # --- 3. Basic Text Generation (Single Turn) ---
    print("\n" + "="*50)
    print("--- Basic Text Generation (Single Turn) ---")
    print("="*50)

def prompt_receiving(prompt, max_tokens_len=200):
    model = GPT4All(MODEL_NAME, allow_download=False)
    logger.info(f"Prompt: {prompt}")
    start_time = time.time()
    response = model.generate(prompt, max_tokens=max_tokens_len, temp=0.2)
    end_time = time.time()
    print(f"GPT response: {response}")
    logger.info(f"Generated in {end_time - start_time:.2f} seconds.")

# =================  Examples below:
# prompt1 = "Tell me a short story"
# logger.info(f"Prompt 1: {prompt1}")
# start_time = time.time()
# response1 = model.generate(prompt1, max_tokens=100, temp=0.7)
# end_time = time.time()
# print(f"AI: {response1}")
# logger.info(f"Generated in {end_time - start_time:.2f} seconds.")

# # --- 4. Streaming Text Generation ---
# # This is great for interactive applications where you want to show output as it's generated.
# print("\n" + "="*50)
# print("--- Streaming Text Generation ---")
# print("="*50)

# prompt2 = "Explain the concept of quantum entanglement in simple terms."
# logger.info(f"Prompt 2: {prompt2}")
# print("AI (streaming): ", end="")
# start_time = time.time()
# full_streaming_response = ""
# for token in model.generate(prompt2, max_tokens=150, temp=0.5, streaming=True):
#     print(token, end='', flush=True) # `flush=True` is important for immediate output
#     full_streaming_response += token
# end_time = time.time()
# print("\n(End of streaming response)")
# logger.info(f"Generated in {end_time - start_time:.2f} seconds.")

# # --- 5. Maintaining Conversational Context with chat_session() ---
# # The chat_session context manager automatically manages message history.
# print("\n" + "="*50)
# print("--- Conversational Chat Session ---")
# print("="*50)

# with model.chat_session():
#     user_input_1 = "Hi, what's your name?"
#     logger.info(f"User 1: {user_input_1}")
#     response_chat_1 = model.generate(user_input_1, max_tokens=30)
#     print(f"AI: {response_chat_1}")

#     user_input_2 = "And what is your purpose?"
#     logger.info(f"User 2 (contextual): {user_input_2}")
#     response_chat_2 = model.generate(user_input_2, max_tokens=50)
#     print(f"AI: {response_chat_2}")

#     # user_input_3 = "Can you rephrase your last answer for a 5-year-old?"
#     # logger.info(f"User 3 (contextual): {user_input_3}")
#     # response_chat_3 = model.generate(user_input_3, max_tokens=70)
#     # print(f"AI: {response_chat_3}")

# # --- 6. Using the 'messages' API (OpenAI-like format) ---
# # This gives you explicit control over roles (system, user, assistant)
# # and is useful for fine-tuning model behavior.
# print("\n" + "="*50)
# print("--- Messages API (OpenAI-like) ---")
# print("="*50)

# messages = [
#     {"role": "system", "content": "You are a friendly, concise, and helpful assistant. Always respond in rhymes."},
#     {"role": "user", "content": "Tell me about the weather today."},
# ]
# logger.info("Messages API prompt initiated.")
# response_messages_1 = model.generate(messages, max_tokens=60, temp=0.8)
# print(f"AI: {response_messages_1}")

# messages_2 = [
#     {"role": "user", "content": "Tell me a fun fact about cats."}
# ]
# logger.info("Messages API (no system message) prompt initiated.")
# response_messages_2 = model.generate(messages_2, max_tokens=60, temp=0.8)
# print(f"AI: {response_messages_2}")


# # --- 7. Listing Available Models (Programmatic) ---
# print("\n" + "="*50)
# print("--- Listing Available Models ---")
# print("="*50)

# try:
#     logger.info("Fetching list of available GPT4All models...")
#     available_models = get_model_list()
#     if available_models:
#         print("Models available for download (showing first 5 GGUF models):")
#         count = 0
#         for m in available_models:
#             if m.get("filename", "").endswith(".gguf") and count < 5: # Filter for modern GGUF models
#                 print(f"  - Filename: {m['filename']}")
#                 print(f"    Size: {round(m['filesize'] / (1024*1024), 2)} MB")
#                 print(f"    Description: {m['description']}")
#                 print("-" * 20)
#                 count += 1
#             elif count >= 5:
#                 break
#         if count == 0:
#             print("No GGUF models found in the list.")
#     else:
#         print("Could not retrieve the list of available models. Check internet connection.")
# except Exception as e:
#     logger.error(f"Error fetching model list: {e}")

# print("\n" + "="*50)
# print("--- Example Finished ---")
# print("="*50)