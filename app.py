import google.generativeai as genai

# اپنی API Key یہاں لگائیں
API_KEY = "AQ.Ab8RN6J-RVd5lPmGwnPRSMXXaY_0UwZy8DCWmxPzGuQr-MwP9w"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-flash-latest")

# اپنا سارا ڈیٹا یہاں پیسٹ کریں
knowledge_base = """
Name: Musa Khan  
Age: 47  
father Name : Eisa Khan 
Brother : Ibrahim Khan
Married in 1997 
Education: Matric 
Job: Government employee in Revenue Department   
Salary : approximate 70k 
Experience: 27 years  
Location: Chowk Sarwar Shaheed  
Personality: Mostly strict but sometimes friendly  
Hobby: Gardening
Phone Number : 03254553366

یہاں اپنی باقی ساری معلومات شامل کریں۔
"""

def ask_chatbot(question):

    prompt = f"""
You are an information assistant.

IMPORTANT RULES:

1. Answer ONLY from the knowledge base.
2. Never use outside knowledge.
3. Never guess.
4. If information is not available, reply EXACTLY:
I have no information about this.
5. Support Urdu and English.

KNOWLEDGE BASE:
{knowledge_base}

QUESTION:
{question}
"""

    response = model.generate_content(prompt)
    return response.text


print("Chatbot Ready!")
print("Type 'exit' to stop.\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    answer = ask_chatbot(question)

    print("\nBot:", answer)
    print()
