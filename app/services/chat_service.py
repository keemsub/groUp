import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_chat_response(question: str) -> str:
    try:
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "너는 이력서 코치야. 간결하고 실용적인 조언을 해줘."},
                {"role": "user", "content": question}
            ]
        )
        return res.choices[0].message.content
    except Exception as e:
        return "에러 발생: " + str(e)