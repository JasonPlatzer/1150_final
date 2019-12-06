import requests
import docx

document = docx.Document()
document.add_paragraph('Random Taco Cookbook', 'Title')
document.add_picture('resizedTaco.jpg')
document.add_paragraph('Credits', 'Heading1')
document.add_paragraph('Photo: Miguel Andrade', 'List Bullet')
document.add_paragraph('Tacos from random taco API URL: https://taco-1150.herokuapp.com/random/?full_taco=true', 'List Bullet')
document.add_paragraph('Code by Jason Platzer', 'List Bullet')
document.add_page_break()
for responses in range(3):
    response = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()
    base = response['base_layer']['recipe']
    seasoning = response['seasoning']['recipe']
    mix = response['mixin']['recipe']
    condiment = response['condiment']['recipe']
    shell = response['shell']['recipe']
    base_name = response['base_layer']['name']
    seasoning_name = response['seasoning']['name']
    mixin_name = response['mixin']['name']
    condiment_name = response['condiment']['name']
    shell_name = response['shell']['name']
    p = document.add_paragraph(base_name, 'Title')
    p.add_run(' with ')
    p.add_run(seasoning_name)
    p.add_run(' and ' )
    p.add_run(condiment_name)
    p.add_run(' in ')
    p.add_run(shell_name)
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