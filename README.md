# Employee-Management-System
Aim of this project is to provide an application for the management of company's blog and employees working under it. It stores large amount of data such as thousands of employees with there name, role and the other details. CRUD operations are widely used in many applications that are supported by underlying relational databases. These four basic CRUD functions are incredibly versatile in how they can support a variety of important functions across different business models and industry verticals.

![Screenshot 2023-08-24 181624](https://github.com/sricharan959/Employee-Management-System/assets/115167414/27283737-414f-47b4-bc7a-2592d992a8c3)
The four CRUD functions can be called by users to perform different types of operations on selected data within the database. This could be accomplished using code or through a graphical user interface. Let's review each of the four components in-depth to fully appreciate their collective importance in facilitating database interactions.
### How to Deploy and Run
1. Fork the repository to your account.
2. Clone the repository to your system.
3. Open the terminal in project folder and type the following:
   
    ```
   ./learnDjango/Scripts/Activate.ps1
   python manage.py runserver
    ```
5. Open localhost site
## Funtionality
### Add a New Employee
The CREATE operation adds a new record to a database. In RDBMS, a database table row is referred to as a record, while columns are called attributes or fields. The CREATE operation adds one or more new records with distinct field values in a table.

![Screenshot 2023-08-24 182043](https://github.com/sricharan959/Employee-Management-System/assets/115167414/4009a754-453d-4983-ba3f-81b0b3338490)

### Delete an Existing Employee
DELETE operations allow the user to remove records from the database. A hard delete removes the record altogether, while a soft delete flags the record but leaves it in place. For example, this is important in payroll where employment records need to be maintained even after an employee has left the company.

![Screenshot 2023-08-24 182212](https://github.com/sricharan959/Employee-Management-System/assets/115167414/29e503e6-583f-40c1-9342-4e48c847b205)
![Screenshot 2023-08-24 181916](https://github.com/sricharan959/Employee-Management-System/assets/115167414/6b162029-42bd-4236-92f8-688536d39180)
### Update an Existing Employee
UPDATE is used to modify existing records in the database. For example, this can be the change of address in a customer database or price change in a product database. Similar to READ, UPDATEs can be applied across all records or only a few, based on criteria.

An UPDATE operation can modify and persist changes to a single field or to multiple fields of the record. If multiple fields are to be updated, the database system ensures they are all updated or not at all. Some big data systems don’t implement UPDATE but allow only a timestamped CREATE operation, adding a new version of the row each time.

![Screenshot 2023-08-24 182005](https://github.com/sricharan959/Employee-Management-System/assets/115167414/99a60335-9319-4c5b-8086-0271a3eab173)
### Read the Blog
READ returns records (or documents or items) from a database table (or collection or bucket) based on some search criteria. The READ operation can return all records and some or all fields.

![Screenshot 2023-08-24 181828](https://github.com/sricharan959/Employee-Management-System/assets/115167414/d3d0b61d-e924-4441-aa19-437dd9bb6359)
## Framworks:
Django 4.0
Bootstrap v5.2


