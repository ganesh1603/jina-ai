import requests
from typing import Optional
import streamlit as st

BASE_API_URL = "https://langflow-f6b676648a.wolf.jina.ai/api/v1/process"
FLOW_ID = "caddf5de-d712-41a2-9084-3745b7947154"
# You can tweak the flow by adding a tweaks dictionary
# e.g {"OpenAI-XXXXX": {"model_name": "gpt-4"}}
TWEAKS = {
  "Cohere-uGh0h": {},
  "ConversationChain-YnzXP": {}
}

def run_flow(inputs: dict, flow_id: str, tweaks: Optional[dict] = None) -> dict:
    """
    Run a flow with a given message and optional tweaks.

    :param message: The message to send to the flow
    :param flow_id: The ID of the flow to run
    :param tweaks: Optional tweaks to customize the flow
    :return: The JSON response from the flow
    """
    api_url = f"{BASE_API_URL}/{flow_id}"

    payload = {"inputs": inputs}

    if tweaks:
        payload["tweaks"] = tweaks

    response = requests.post(api_url, json=payload)
    return response.json()

# Setup any tweaks you want to apply to the flow
inputs = {"input":"write about twitter"}
st.write(run_flow(inputs, flow_id=FLOW_ID, tweaks=TWEAKS))
