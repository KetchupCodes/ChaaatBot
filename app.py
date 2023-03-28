from flask import Flask, request, jsonify
from flask_cors import CORS

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
import os
os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "f02a5a96c8a6199fd82889ddec34f2edc56d464e842a28d3fa4f9f1997bc3f54"
chat = ChatOpenAI(openai_api_key="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")

llm = OpenAI(temperature=0)
app = Flask(__name__)
CORS(app)
@app.route('/chatbot', methods=['POST'])
def chatbot():
    message = request.json.get('message', '')
    
    messages = [SystemMessage(content="I am in Bengaluru, You are a local and will be my tourguide. You will always be factually accurate and give real data."),
    HumanMessage(content=f"Suggest some restaurants where i can eat {message}")]
    
    response = chat(messages).content

    return jsonify({"response": response})
if __name__ == '__main__':
    app.run(debug=True)
