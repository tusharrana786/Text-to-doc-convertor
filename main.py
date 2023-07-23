from docxtpl import DocxTemplate
doc = DocxTemplate("template.docx")
sample_text = input("Enter Text")
context = {'test': sample_text}
doc.render(context)
doc.save("generated.docx")