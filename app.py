import streamlit as st
import requests


API_URL_GPT35 = "http://localhost:9800/gpt35/generate-code/"
API_URL_GPT40 = "http://localhost:9800/gpt40/generate-code/"


def getCodeForQueryUsingGpt35(prompt):	
	message = {'prompt':prompt,}
	response = requests.post(url = API_URL_GPT35, params = message)	
	if response.status_code==200:
		return response.json()
	else:
		return None


def getCodeForQueryUsingGpt40(prompt):	
	message = {'prompt':prompt,}
	response = requests.post(url = API_URL_GPT40, params = message)	
	if response.status_code==200:
		return response.json()
	else:
		return None


def main():
	st.title("Automated Code Generation!")
	st.write()
	st.subheader("Please fill the below details.")
	userPrompt = st.text_input("Please describe your requirement to generate code.")
	modelOptions = ["ChatGPT-4", "ChatGPT-3.5"]
	model = st.selectbox("Choose the model you want to use.", modelOptions)


	if(st.button("Generate Code", type = "primary")):
		if (len(userPrompt) >0) and (len(model) > 0 ):
			promptString = "Please write a code for the given requirement. Please make relevant assumtions. Also, please explain the steps of your approach before writing code for the given requirement. The description of the requirement is : {userPrompt}"
			prompt = promptString.format(userPrompt=userPrompt,)
			prompt = prompt.strip().encode('utf-8')
			st.subheader("Generated Code")

			if model == "ChatGPT-3.5" :
				code = getCodeForQueryUsingGpt35(prompt)
				st.write(code)


			if model == "ChatGPT-4" :
				code = getCodeForQueryUsingGpt40(prompt)
				st.write(code)

		else:
			st.write("All fields are necessary")



	st.write("---")


if __name__ == "__main__":
	main()