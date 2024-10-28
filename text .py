import pywhatkit as pw
text="""python is an interpreted high-level genrel-purpose programming language.
its design philosophy emphasizes code rabidility with its use of signification indentation."""
pw.text_to_handwriting(text,"demo1.png",[0,0,138])
print ("End") 





# import pywhatkit as pw

# # Define the text to convert
# text = """Python is an interpreted high-level general-purpose programming language.
# Its design philosophy emphasizes code readability with its use of significant indentation."""

# # Convert text to handwriting and save it as 'demo1.png'
# pw.text_to_handwriting(text, "demo1.png",