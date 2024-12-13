from fpdf import FPDF

pdf = FPDF(orientation = "P", unit = "pt", format="A4")
pdf.add_page()

pdf.image('killer.PNG',w=100, h=80)

#TITLE
pdf.set_font(family="Times",style="B", size=24)
pdf.cell(w=0, h=50, txt = "TEST FOR JEM APPRU", align="C", border=1, ln=1)

#subheading
pdf.set_font(family="Times",style="B", size=14)
pdf.cell(w=0, h=15, txt = "Description", ln =1)

#body
pdf.set_font(family="Times", size=12)
txt1 = """
The Battle of Alton (also Storm of Alton),[7] of the First English Civil War, took place on 13 December 1643 in the town of Alton, Hampshire, England. There, Parliamentary forces serving under Sir William Waller led a successful surprise attack on a winter garrison of Royalist infantry and cavalry serving under the Earl of Crawford.[3] The Battle of Alton was the first decisive defeat of Sir Ralph Hopton, leader of Royalist forces in the south, and the event had a significant psychological effect on him as commander.[7] More important to Hopton was the loss of men, however, as he was already short-handed in much-needed infantry. The successful Parliamentarians were able, after their victory, to attack and successfully besiege Arundel, a larger and more formidable Royalist outpost to the south-east of Alton.[2]

"""
pdf.multi_cell(w=0, h=15, txt = txt1)


pdf.output('output.pdf')