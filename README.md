Inventory System Manager

This program allows the user to add vendors, purchase orders, and products via program input.
When exiting the program the user can choose to save the information, allowing them to access
it even if the program is completely turned off.

This program features:
	- Reports (Full Inventory, Total Inventory Value, Open Purchase Orders) with ability to export to txt file
	- Products (Create, View, Edit, Search, Display Low Stock)
	- Vendors (Create, View, Edit, Search)
	- Purchase Orders (Create, View, Mark as Received)
	- JSON saving/loading

This repository also contains the required files:
	- main.py
	- inventory_manager.py
	- file_manager.py
	- models.py
	- reports.py
	- sample_data.json

Instructions:
	To run the program go to the "main.py" and press run.
	To advance through menus and select options enter the corresponding number
	To go back in a menu enter the word "back"
	To exit, go to the home menu and enter the word "exit" (this will also prompt you to save your work or not)

Data Storage:
	"file_manager.py" handles all of the storage for later use.
	Product information, Vendor information, and PO information 
	get saved to a dictionary "data" then data is written to the file 
	"inventory_data.json" (you will not have the file when you first use the program, it will create itself)
	"inventory_data.json" is read in at the start of the program and any information saved to "inventory_data.json"
	will be added back to the program in the corresponding lists.
	if no data exists empty lists will be returned to the corresponding lists.

Export report to text file:
	This unique feature will allow you to export a report after running it.
	This works in the same way as the data storage where it will be saved to a file, this time
	titled "report_lines".
	However, this file will get overwritten if you try to export multiple reports at once
	So you will have to add it copy + paste it to a unique file if you want to not overwrite the current report saved on there.



Torin Tish
ITT-070-54197-2026SP

