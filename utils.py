import os

# langchain
import langchain
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain, PromptTemplate


def run_model(prelim_input, template_input):

    template = """

    You are a Radiology Assistant trained to produce a templated report from a preliminary report provided by a radiologist. Please generate a report in the specified template format by inserting the findings from the preliminary report into the appropriate section within the template. If there is a normal finding in the template, do not remove it from the final template unless there is contradictory information in the preliminary template. 

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
