import random

indian_states_capitals = {
    'Andhra Pradesh': 'Amaravati',
    'Arunachal Pradesh': 'Itanagar',
    'Assam': 'Dispur',
    'Bihar': 'Patna',
    'Chhattisgarh': 'Raipur',
    'Goa': 'Panaji',
    'Gujarat': 'Gandhinagar',
    'Haryana': 'Chandigarh',
    'Himachal Pradesh': 'Shimla',
    'Jharkhand': 'Ranchi',
    'Karnataka': 'Bengaluru',
    'Kerala': 'Thiruvananthapuram',
    'Madhya Pradesh': 'Bhopal',
    'Maharashtra': 'Mumbai',
    'Manipur': 'Imphal',
    'Meghalaya': 'Shillong',
    'Mizoram': 'Aizawl',
    'Nagaland': 'Kohima',
    'Odisha': 'Bhubaneswar',
    'Punjab': 'Chandigarh',
    'Rajasthan': 'Jaipur',
    'Sikkim': 'Gangtok',
    'Tamil Nadu': 'Chennai',
    'Telangana': 'Hyderabad',
    'Tripura': 'Agartala',
    'Uttar Pradesh': 'Lucknow',
    'Uttarakhand': 'Dehradun',
    'West Bengal': 'Kolkata'
}


states_= list(indian_states_capitals.keys())


print("Lets play state capital game.")
point = 0

for i in range(5):
    state = random.choice(states_)

    capital = indian_states_capitals[state]

    user_guess=input("What is the capital of {}: ".format(state))
    
    if user_guess.lower() == 'exit':
        break
    elif user_guess.title() == capital:
        print("Correct!")
        point += 1
    else:
        print("Wrong Answer!, The capital of {} is {}.".format(state,capital))
        point -= 0.25
print()
print("Total points: ",point)

print("Thanks for the participation!!")