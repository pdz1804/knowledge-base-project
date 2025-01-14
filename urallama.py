import requests
import json


class URAWrapper:
    headers = {
        "Content-Type": "application/json",
        "Authorization": "BGZSrOW9Xat5maxibhdmMQh5IoJADSSzzwJRvXmhswzhYbJGUaCxOegpDTM6x6ywtbxVHBk5z0aELkYG1MKpfsyqq5YPCZ6beDGm0eJ39ErCUg4cDCj72rizFEEhKaic",
    }

    def predict(self, input: str):
        data = {
            "model": "ura-llama-7b-q4",
            "raw": True,
            "prompt": input,
            "stream": False,
            "options": {
                "stop": ["</s>", "[INST]", "/.", "[INST:"],
                "temperature": 0.1,
                "top_k": 50,
                "top_p": 0.9,
            }
        }

        answer = requests.post(
            url='https://www.ura.hcmut.edu.vn/ollama/api/generate',
            headers=self.headers,
            data=json.dumps(data)
        )

        if answer.status_code == 200:
            return answer.json()['response'].strip()

        return -1


class URALocalWrapper:
    headers = {
        "Content-Type": "application/json"
    }

    def predict(self, input: str):
        data = {
            "model": "ura-llama-7b",
            "prompt": input,
            "stream": False,
            "stop": ["</s>", "[INST]", "/.", "[INST:"],
            "max_tokens": 512,
            "temperature": 0.1,
            "top_k": 50,
            "top_p": 0.9,
        }

        answer = requests.post(
            url='http://127.0.0.1:5000/v1/completions',
            headers=self.headers,
            data=json.dumps(data)
        )

        if answer.status_code == 200:
            return answer.json()['choices'][0]['text'].strip()

        return -1


# model = URALocalWrapper()
#
# print(model.predict(
#     "[INST] Sau thứ bảy là thứ mấy? [/INST]"
# ))
