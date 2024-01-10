#function to interactive chat
#type "end" to finish the multi-turn dialog
#output a pretty summary of the conversation
def dialog():
    global history
    q = input("enter your question:")
    response, history = model.chat(tokenizer, query=q, history=history)
    print(response)
    if q == "end":
        pretty_print()
        return None
    else:
        dialog()


#formats the conversation into readable USER and ASSISTANT organized output
def pretty_print():
    for turn in history:
        print("USER: " + turn[0])
        print("ASSISTANT: " + turn[1])
	print(" ")

