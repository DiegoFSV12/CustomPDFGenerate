import streamlit as st
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        if hasattr(self,'document_tittle'):
            self.set_font('Arial','B',12)
            self.cell(0,10,self.document_title,0,1,'C')
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial','I',8)
        self.cell(0,10,f'Página{self.page_no()}',0,0,'C')
    
    def chapter_title(self,title,font='Arial',size=12):
        self.set_font(font,'B',size)
        self.cell(0,10,title,0,1,'L')
        self.ln(10)#Separa lo que le siga al titulo del capitulo
    
    def chapter_body(self,body,font='Arial',size=12):
        self.set_font(font,'',size)
        self.multi_cell(0,10,body)
        self.ln()

    def create_pdf(filename,document_title,author,chapters,image_path=None):
        pdf = PDF()
        pdf.document_title = document_title
        pdf.add_page()
        if author:
            pdf.set_author(author)
        if image_path:
            pdf.image(image_path,x=10,y=25,w=pdf.w - 20)#Ancho del pdf - 20px
            pdf.ln(120)
        
        for chapter in chapters:
            title, body, font, size = chapter
            pdf.chapter_title(title,font,size)
            pdf.chapter_body(title,body,font,size)
        
        pdf.output(filename)

