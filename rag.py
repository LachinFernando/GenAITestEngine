import os
import base64
import requests

import streamlit as st
from openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI


QA_MODEL = "gpt-4o-mini"

# keys
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# create client
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def get_model():
    model = ChatOpenAI(model=QA_MODEL, api_key=os.environ["OPENAI_API_KEY"])
    return model


def streaming_question_answering(requirements: str, template: str):
    prompt = ChatPromptTemplate.from_template(template)
    model = get_model()
    output_parser = StrOutputParser()

    # create the chain
    chain = prompt | model | output_parser

    # get the answer
    return chain.stream({"requirements": requirements})


def streaming_question_answering_code(code: str, template: str):
    prompt = ChatPromptTemplate.from_template(template)
    model = get_model()
    output_parser = StrOutputParser()

    # create the chain
    chain = prompt | model | output_parser

    # get the answer
    return chain.stream({"code": code})