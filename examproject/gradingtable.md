# DAT310 2021 Exam project grading table

The table below contains detailed criteria how projects are graded.
Criteria are explained below.

| Criteria                 | %   |
| ------------------------ | --- |
| Report                   | 5%  |
| **Frontend**             |     |
| Login                    | 3%  |
| Register                 | 3%  |
| Form validation          | 3%  |
| Collection display       | 2%  |
| Sorting/filtering        | 3%  |
| Search                   | 4%  |
| User preferences         | 3%  |
| Components separation    | 5%  |
| JS routing               | 4%  |
| Update                   | 3%  |
| Delete                   | 3%  |
| Understandable code      | 5%  |
| Additional functionality | 10% |
| **Design**               |     |
| Fluid layout basic       | 5%  |
| Nice, advanced layout    | 5%  |
| **Database**             |     |
| Has 3 tables             | 4%  |
| delete&update            | 3%  |
| advanced                 | 3%  |
| **Backend**              |     |
| REST api                 | 8%  |
| Validation               | 5%  |
| Access control           | 5%  |
| Extra features           | 6%  |

## Report

Report should contain:
- Topic of the application
- Database layout, e.g. name tables
- Simple design (drawing, ...)

Points are only given, if report topic matches application topic.

## Frontend

- **Login:** Possible to log in and out with different users
- **Register:** Possible to register new users
- **Form validation:** Errors are displayed, e.g. when username is taken. Also register should not allow empty password.
- **Display of collection:** List or table to display items from database.
- **Sorting/Filtering:** Ability to sort or filter item list.
- **Search:** Search for items using text input.
- **User preferences:** Some setting on look, sort or search is stored, either in database or cookie/local storage.
- **Components:** Frontend code is separated into components.
- **Routing:** Some form of routing is implemented, typically using Vue-Router.
- **Update:** Possible to add end edit data.
- **Delete:** Possible to delete data.
- **Understandable code:** Looking at individual components, it is easy to understand their use and they show no obvious flaws.
- **Complex functionality:** Extra points for all kind of complex or additional functionality. Examples are:
    * Image upload (7%)
    * Handling of dates (2-5%)
    * Extensive form validation, e.g. password criteria, username length, ...
    * Extensive configurability, e.g. all items editable/deletable by admin, ...

## Layout

- **Fluid layout:** Layout adapts to screen size. If bootstrap is used, adapting to phone size is necessary.
- **Nice, advanced layout:** Looks good, adapts to screen by changing appearance.

## Database

- **3 tables:** Database contains at least 3 tables
- **Update/Delete:** Database data is updated and deleted.
- **Advanced:** Any more advanced feature, including additional tables, database functions e.g. MAX, detailed access functions, ... 

## Backend

- **REST api** A rest api, without verbs in route names, using JSON data format, e.g. `/item/<int:itemid>, methods=["PUT"]` instead of `/updateitem`.
- **Validation** on registration, check server side that username, password are not empty, or more.
- **Access control** for routes that should only be accessed with login, this is checked server side.
- **Extra features** includes
   * extensive validation, 
   * extensive API, allowing to update and delete different data,
   * storage of images
   * other functionality