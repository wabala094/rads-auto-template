import os

# langchain
import langchain
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain, PromptTemplate


def run_model(prelim_input, template_input):

    template = """

    You are Assistant, a large language model trained by OpenAI that focuses on assiting radiologists with their work. \
    In particular, Assistant is an expert at taking a preliminary report from a radiologist and placing the findings\
    into the provided templated standard report format for easy readability by other clinicians. Only replace or remove any words unless it woould be \
    contradictory to include them.


    The only goal of the Assistant is to produce the templated report. This is the only response.

    Preliminary Report: {prelim}

    Template: {rads_template}

    """

    prompt = PromptTemplate(
        input_variables = ["prelim", "rads_template"],
        template=template)


    llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)
    chain = LLMChain(llm=llm, prompt=prompt)

    prompt_inputs = {
        'prelim': prelim_input,
        'rads_template': template_input
    }

    output = chain.run(prompt_inputs)

    return output
