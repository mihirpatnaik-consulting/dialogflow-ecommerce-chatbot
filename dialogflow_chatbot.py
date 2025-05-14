import os
from google.cloud import dialogflow_v2 as dialogflow

# Set up Google Cloud credentials (replace with your service account key path)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/service-account-key.json"

# Dialogflow project ID and session ID
project_id = "datasenceai-es"  # Replace with your Dialogflow project ID
session_id = "unique-session-id-123"

# Initialize Dialogflow session client
session_client = dialogflow.SessionsClient()
session = session_client.session_path(project_id, session_id)

def detect_intent_text(text, language_code="en"):
    """Sends a text query to Dialogflow and returns the response."""
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    
    try:
        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )
        return response.query_result.fulfillment_text
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage for e-commerce queries
if __name__ == "__main__":
    queries = [
        "What are your store hours?",
        "Do you have free shipping?",
        "How can I track my order?"
    ]
    
    for query in queries:
        print(f"User: {query}")
        response = detect_intent_text(query)
        print(f"Bot: {response}\n")