"""2-5. Famous Quote: Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks:
Albert Einstein once said, “A person who never made a mistake never
tried anything new.”"""

quote = "A person who never made a mistake never tried anything new."
author = "Albert Einstein\t"
message = f"{author} once said, \"{quote}\""
print(message)


"""2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous
person’s name using a variable called famous_person. 
Then compose your message and represent it with a new variable called message. Print your message."""

famous_persons, message = input("Enter famous persons names: "), input("Enter mssage: ")
print(f"Your famous person's name is {famous_persons} and your message is {message}")
