from pyscript import display, document


def intrams_qualifications(e):
    document.getElementById('output').innerHTML = ''

    registration = document.querySelector('input[name="registration"]:checked').value
    medcert = document.querySelector('input[name="medical"]:checked').value
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value

    teams = {
        ("7", "Sapphire"): "Blue Bears",
        ("8", "Sapphire"): "Red Bulldogs",
        ("9", "Sapphire"): "Green Hornets",
        ("10", "Sapphire"): "Yellow Tigers",

        ("7", "Emerald"): "Red Bulldogs",
        ("8", "Emerald"): "Yellow Tigers",
        ("9", "Emerald"): "Blue Bears",
        ("10", "Emerald"): "Green Hornets",

        ("7", "Ruby"): "Yellow Tigers",
        ("8", "Ruby"): "Green Hornets",
        ("9", "Ruby"): "Red Bulldogs",
        ("10", "Ruby"): "Blue Bears",

        ("7", "Topaz"): "Green Hornets",
        ("8", "Topaz"): "Blue Bears",
        ("9", "Topaz"): "Red Bulldogs",
        ("10", "Topaz"): "Yellow Tigers",
    }

    team = teams.get((grade, section))

    # eligibility
    if registration == 'Yes_reg' and medcert == 'Yes_med':
        display(f'Congratulations! You can play.', target='output')
    elif registration == 'No_reg':
        display(f'You cannot play. You have to register.', target='output')
    elif medcert == 'No_med':
        display(f'You cannot play because you do not have a medical certificate.', target='output')
    else:
        display(f'invalid input', target='output')
    
    # confirmation
    if team:
        display(
            f" Your team is: {team}",
            target="output"
        ) 
