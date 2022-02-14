from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Frame
from reportlab.lib.styles import getSampleStyleSheet


#platypus updated

def main():
	reportName = input("Please Enter a Preferred Report Name:\n")
	inputText = input("Please Enter the Input File:\n")
	reportTitle = input("Please Enter the Report Title:\n")
	reportAuthor = input("Please Enter the Report Author:\n")
	try:
		generateReport(reportName,inputText,reportTitle,reportAuthor)
		print("Successfully created report")
	except Exception as e:
		print(f"Error in creating report:\n{e}")

def generateReport(rN,iT,rT,rA):
	styles = getSampleStyleSheet()
	styleN = styles['Normal']
	styleH = styles['Heading1']
	styleh = styles['Heading3']
	story = []

	pdf_name = f'{rN}.pdf'
	doc = SimpleDocTemplate(
		pdf_name,
		pagesize=letter,
		bottomMargin=.4 * inch,
		topMargin=.6 * inch,
		rightMargin=.8 * inch,
		leftMargin=.8 * inch,
		title = rT,
		creator = rA,
		author = rA,
		keywords = [],
		)

	with open(iT, "r") as txt_file:
		text_content = txt_file.read()

	P = Paragraph(text_content, styleN)
	story.append(Paragraph(rT,styleH))
	story.append(Paragraph(f'Author: {rA}',styleh))
	story.append(P)

	doc.build(
		story,
	)

main()
