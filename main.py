import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import system_prompt
from call_function import *
import json

def main():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if api_key == None:
        raise RuntimeError("API key not found.")
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    parser = argparse.ArgumentParser(description="Chat with OpenRouter API")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": args.user_prompt
        },
    ]

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
        )

    message = response.choices[0].message

    for tool_call in message.tool_calls:
        result_message = call_function(tool_call, args.verbose)
        if len(result_message["content"]) == 0:
            raise Exception("Error: function returned no content")
        else:
            if args.verbose:
                if response.usage is not None:
                    print(f"Prompt tokens: {response.usage.prompt_tokens}")
                    print(f"Response tokens: {response.usage.completion_tokens}")
                else:
                    raise RuntimeError("Response usage is None. Something went wrong.")

                print(f'User prompt: {messages[1]["content"]}')
                print(f'-> {result_message["content"]}')
            else:
                print(message.content)


if __name__ == "__main__":
    main()
