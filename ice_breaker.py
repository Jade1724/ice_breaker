import os

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import fetch_profile_from_gist

if __name__ == '__main__':

    summary_template = """
    given the Linkedin information {information} about a person I wnat you to create:
    1. A short summary
    2. two interesting facts about them 
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = fetch_profile_from_gist()
    print(linkedin_data.json())
