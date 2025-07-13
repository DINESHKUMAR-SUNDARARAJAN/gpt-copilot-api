import requests

BASE_URL = "http://localhost:8000"

def test_chat(user_id: str, query: str):
    print(f"Query: {query}")
    response = requests.post(
        f"{BASE_URL}/chat/stream",
        json={"user_id": user_id, "query": query},
        stream=True
    )

    print("Streamed response:")
    for line in response.iter_lines():
        if line:
            print(line.decode("utf-8"), end="", flush=True)
    print("\nDone")



def test_upload(user_id: str, file_path: str):
    print(f"Uploading file: {file_path} for user: {user_id}")
    with open(file_path, "rb") as f:
        response = requests.post(f"{BASE_URL}/upload/" + user_id, files={"file": f})
    print("Upload Response:", response.json())


if __name__ == "__main__":
    # Update this to your test user and file
    user = "dinesh"
    pdf_path = "engineering_handbook.pdf"

    # 1. Upload a PDF
    test_upload(user, pdf_path)

    # 2. Ask a question about the uploaded document
    test_chat(user, "What is our onboarding process?")

    # 3. Ask a follow-up question to check memory + RAG
    test_chat(user, "What is our onboarding policy and background check policy and what is 12 divided by 4.5? and also todays date in milan")
