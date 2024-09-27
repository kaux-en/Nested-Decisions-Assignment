#Quick decisions: The Event Planner

#Task 1: Code Correction
attendees = int(input("Enter number of attendees:"))
venue = "large hall" if attendees > 100 else "conference room" 
print(venue)

#Task 2: Venue Selection
audio_system = "on" if attendees >= 50 else "off"
print(audio_system)
projector = "In use" if attendees >= 20 else "off"
print(projector)

#Task 3: Catering Choices
catering = input("Do you prefer Vegetarian food? (yes/no)")

if catering == 'yes':
    print("Veggie Delight Caterers")
else:
    print("Gourmet Meals Caterers")