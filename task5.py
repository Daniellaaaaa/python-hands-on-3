"""
    You're cleaning up your phone's contact list and organizing your close friends from Jos.
    Your friends list is: friends = ["Aisha", "Daniel", "Esther", "John", "Mary", "Paul", "Ruth"]
    
    1. You made a new close friend "Kemi" and want to add her between "John" and "Mary".
    2. "Daniel" moved to Lagos and you don't talk anymore, so remove him from your close friends list.
    3. "Aisha" got married and now goes by "Aisha_M". Update her name in the list.
    4. You want to add your cousin "Zainab" at the end of the list.
    5. Create a new list with only the first 3 friends from your updated list and display it.
    6. Find out what position "Paul" is in your final friends list (remember: position counting starts from 1 for humans!).
    7. arrange your contacts in Descending Alphabetical Order using.
"""

# Question 1
friends = ["Aisha", "Daniel", "Esther", "John", "Mary", "Paul", "Ruth"]
friends.insert(4, "Kemi")
print("1. ", friends)
# Question 2
friends.remove(friends[1])
print("2. ", friends) 
# Question 3
friends[0]="Aisha_M"
print("3. ", friends)
# Question 4
friends.append("Zainab")
print("4. ", friends)
# Question 5
friends2=friends[0:3]
print("5. ", friends2)
# Question 6
print("6. 6")
# Question 7
srt=sorted(friends)
print("7. " ,srt[::-1])
