from study7_5 import letter

response = {
    'salutation': 'Colonel',
    'name': 'Hackenbush',
    'product': 'duck blind',
    'verbed': 'imploded',
    'room': 'conservatory',
    'animals': 'emus',
    'amount': '$1.38',
    'percent': '1',
    'spokesman': 'Edgar Schmeltz',
    'job_title': 'Licensed Podiatrist',
}

print(letter.format(**response))
