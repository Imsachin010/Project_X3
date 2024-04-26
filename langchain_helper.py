import os
from langchain.llms import OpenAI
from langchain_community.llms import OpenAI
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from secret_key import openapi_key

os.environ['OPENAI_API_KEY'] = "sk-proj-KXSRAuZ0pxgSzKvoCo4nT3BlbkFJY8fCiu98EyqWiumVORRx"

llm = OpenAI(temperature=0.7)


def generate_restaurant_name_and_item(cuisine):

  #1 restaurant name
  prompt_template_name = PromptTemplate(
      input_variables=['cuisine'],
      template=
      "I want to open a restaurant for {cuisine} food. suggest a fancy name for this."
  )
  name_chain = LLMChain(llm=llm,
                        prompt=prompt_template_name,
                        output_key="restaurant_name")

  #2 menu items
  prompt_template_items = PromptTemplate(
      input_variables=['restaurant_name'],
      template=
      """Suggest some food menu items for {restaurant_name}. Returm it as a comma seprated"""
  )
  food_item_chain = LLMChain(llm=llm,
                             prompt=prompt_template_items,
                             output_key='menu_items')

  chain = SequentialChain(chains=[name_chain, food_item_chain],
                          input_variables=["cuisine"],
                          output_variables=["restaurant_name", "menu_items"])

  response = chain({'cuisine': cuisine})

  return response


if __name__ == '__main__':
  print(generate_restaurant_name_and_item('punjabi'))
