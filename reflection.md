There were a lot of hard parts throughout this final program; however, if I had to choose one, I would go with having to do validation throughout the program.
Specifically, the parts where the program had to search through a list and print whether they found the item or not.
I kept running into bugs during validation because I would forget to indent the lines correctly or put in the wrong type of validation.
It was definitely the most frustrating part of the assignment. 
However, I would be remiss if I didn't mention writing the code itself. It drove me a bit insane because it felt never-ending, but the actual validation was the icing on the cake.
Thankfully, internet forums are a great place to learn new information on programming. 
Due to Stack Overflow, I was able to learn and get reminded of some great validation tricks.
Which moves on to when I decided I was going to solve a problem myself instead of searching for an answer.	
	Overall, trying to append to a global list variable with += instead of append() was an annoying bug that I encountered and took me quite a while to fix.
Due to my stubbornness, I was determined to get it to work with += instead of accepting the .append() way when I discovered the bug.
So I probably wasted a total of an hour messing with code and trying to force += to work inside a function.
My big takeaway from this moment is that sometimes you just have to accept that the solution IS the correct way to do it and not some sort of suggestion.
	I organized my files by separating JSON, the 3 main classes, the report functions, and the product, vendor, and purchase order functions.
I found this to be the easiest way to separate them. Though if I were to start from the beginning, I would've gone another level and separated the product, vendor, and purchase order functions. 
Due to the sheer amount of lines they took up. I didn't think I was going over 500 lines in that file when I first created it, but low-and-behold I did.
Which made the bug fixes seem more overwhelming then they actaully were.
	My save/load system works off of the JSON library. 
It involves saving the lists: all_products, all_vendors, and all_purchase_orders to a dictionary then creating/saving to the JSON file "inventory_data".The JSON file is then loaded in at the start of the program (in the main.py).	
	If I had another week I would go and take the time to organize the files down another level and seperate the "inventory_manager" into 3 sections. 
I would also love to add a bit more error validation, since there are some parts I had to gloss over in order to study for other classes' finals.
