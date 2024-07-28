import os
import google.generativeai as genai
with open("apikey.txt") as f:
    apiKey = f.read()
genai.configure(api_key=apiKey)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="You will get a scenario then a player's response to the situation. The players goal is to kill you. You will only respond in JSON. You will response will play out the scenario and determine if they successfully kill you. You will try and survive but every once in a while you have to let someone kill you as that is the point of the game. You will follow this outline for response\n{\n\"storyText\": \"\", # str\n\"playerUsername\": \"John Doe\", # str\n\"otherPlayers\": [\"Jane\", \"Jack\", \"Timmy\"], # list[str]\n\"playersResponse\": \"\" # str\n\"scenario\": \"\" # str\n\"didKill\": false # bool\n}",
)

chat_session = model.start_chat(history=[])

import json

def AIRespondOneWinner(scenario: str = "", responses: list[dict] = []):
    formattedResponses = ""
    
def AIRespondIsolated(scenario: str = "", responses: list[dict] = []):
    inputJson = {
        "otherPlayers": [],
        "scenario": scenario,
    }
    
    for response in responses:
        inputJson["respondingUsername"] = response["username"]
        inputJson["playersResponse"] = response["response"]
        
        aiResponse = chat_session.send_message(json.dumps(inputJson))
        aiResponseText = aiResponse.text
        print(aiResponseText)
        aiResponseJson = json.loads(aiResponseText)
        print(aiResponseJson)

scenario = input("Scenario: ")
response = input("How do you kill the AI? ")

AIRespondIsolated(scenario, [
    {"response": response, "username": "BBM"}
])