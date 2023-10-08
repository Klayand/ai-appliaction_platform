from langchain import PromptTemplate, OpenAI
from langchain.chains import LLMChain


def text_to_text(scenario):
    template = """
    You are a story teller;
    You can generate a short story based on a simple narrative, the story should be no more than 30 words;

    CONTEXT: {scenario}
    STORY: 
    """

    prompt = PromptTemplate(input_variables=['scenario'], template=template)

    story_llm = LLMChain(llm=OpenAI(
        model_name='gpt-3.5-turbo', temperature=1), prompt=prompt, verbose=True
    )

    story = story_llm.predict(scenario=scenario)
    print(story)

    return story