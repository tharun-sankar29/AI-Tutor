from pinecone import Pinecone
from pinecone_plugins.assistant.models.chat import Message
import json

class PineconeWrapper:
	
	def __init__(self):
		self.assistant_name = "pp"
		self.pc = Pinecone(api_key="pcsk_6c1XV3_DN28bio5vSp3DDUnq3a98XRwRNGBcc6Ymc62t39wnJw3VJ5gFHH1C4KbCmqBBN1")
		self.assistant = self.pc.assistant.Assistant(self.assistant_name)

	def executePrompt(self, prompt):
		
		msg = Message(role="user", content=prompt)
		resp = self.assistant.chat(messages=[msg])
		
		result = {
			"content": resp.message.content,
			"citations": []
		}

		for citation in resp.citations:	
			for ref in citation["references"]:
				result["citations"].append({
					"pages": ref["pages"],
					"file": ref["file"]["name"]
				})
		data = json.dumps(result)
		data = json.loads(data)
		result = data["content"]
				
		return result		