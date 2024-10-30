import autogen

person = input("Enter the name: ")

config_list = [{
    "model": "Claude 3.5 Sonnet	",
    "api_key": "YOUR_ANTHROPIC_API_KEY",
    "api_type": "anthropic",
    "max_tokens": 10000
}]

user_proxy = autogen.UserProxyAgent(
    "user",
    code_execution_config={
        "work_dir": "resume",
        "use_docker": False
    },
    human_input_mode= "NEVER",
    is_termination_msg=lambda msg: "TERMINATE" in msg["content"]
)

engineer = autogen.AssistantAgent(
    "engineer",
    llm_config={
        "config_list": config_list
    },
    system_message= "You are a highly skilled AI resume builder. You can create professional and tailored resumes based on user input."
                    "developer. Make sure to have # filename: <name of the file>.py as the first line after the triple tick marks. "
                    "When you are done, reply with TERMINATE.",
)

user_proxy.initiate_chat(
    engineer,
    message=f"""
    Create a professional resume for {person}. Include information on Education, Work and Related Experience, Awards and Honors, Activities/Hobbies, Skills. Format the resume in a clear, visually appealing manner and store it in a file."""
)
