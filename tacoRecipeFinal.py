import requests
import docx

document = docx.Document()
document.add_paragraph('Random Taco Cookbook', 'Title')
document.add_picture('resizedTaco.jpg')
document.add_paragraph('Photo: Miguel Andrade')
document.add_paragraph('random taco API URL: https://taco-1150.herokuapp.com/random/?full_taco=true')
document.add_paragraph('By Jason Platzer')
document.add_page_break()
for responses in range(3):
    response = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()
    base = response['base_layer']['recipe']
    seasoning = response['seasoning']['recipe']
    mix = response['mixin']['recipe']
    condiment = response['condiment']['recipe']
    shell = response['shell']['recipe']
    p = document.add_paragraph()
    document.add_paragraph('Base layer', 'Heading1')
    document.add_paragraph(base)
    document.add_paragraph('Seasoning', 'Heading1')
    document.add_paragraph(seasoning)
    document.add_paragraph('Mixin', 'Heading1')
    document.add_paragraph(mix)
    document.add_paragraph('Condiment', 'Heading1')
    document.add_paragraph(condiment)
    document.add_paragraph('Shell')
    document.add_paragraph(shell)
    document.add_page_break()
    document.save('RandomTacoRecipeBook.docx')