#Estou desenvolvendo um sistema que converte docx e PDF ou o contrario, e utilizando uma interface grafica simple
import PySimpleGUI as sg
from docx import Document
from reportlab.pdfgen import canvas





janela = [
    [sg.Text("Localizar arquivo:"), sg.Input(key="-IN-"), sg.FileBrowse(file_types=(("Word Files", "*.docx"),))],
    [sg.Text("Salvar PDF:"), sg.Input(key="-OUT-"), sg.FileSaveAs(file_types=(("PDF Files", "*.pdf"),))],
    [sg.Button("Converter"), sg.Button("Sair")]
]


window = sg.Window("Converson", janela)
def converte_pdf(entrada, saida):
    doc = Document(entrada)
    text = ""
    for para in doc.paragraphs:
        text += para.text
    c = canvas.Canvas(saida)
    c.drawString(100 , 800 , text)
    c.save()
while True :
    evento, valor = window.read()
    if evento in (sg.WINDOW_CLOSED, "Sair"):
        break
    if evento == "Converter":
        entrada = valor["-IN-"]
        saida = valor["-OUT-"]
        if entrada and saida:
            converte_pdf(entrada, saida)

            sg.popup("conversão ok")
window.close()