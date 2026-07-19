import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse



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
            "role": "user",
            "content": args.user_prompt
        },
    ]

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        )
    
    if args.verbose == True:
        if response.usage is not None:
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")
        else:
            raise RuntimeError("Response usage is None. Something went wrong.")

        print(f"User prompt: {messages[0]["content"]}")
        print(response.choices[0].message.content)
    else:
        print(response.choices[0].message.content)



if __name__ == "__main__":
    main()
