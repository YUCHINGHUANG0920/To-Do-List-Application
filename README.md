## To-Do List Application
### Overview
In this project, I developed a web application using Flask, with a focus on streamlining CRUD (Create, Read, Update, Delete) operations for items within a To-Do List. The application provides users with a seamless experience for adding, viewing, updating, and deleting tasks, enhancing overall task management efficiency.

For data storage, I used MongoDB Atlas as the cloud-based database service. It provides a reliable foundation, enabling the application to handle data and adapt to changing requirements. Therefore, at first, I should find the connection string in my Atlas dashboard. (Go to my cluster --> click "Connect" --> choose "Connect your application". It will provide me with a connection string.) Then, I can create a MongoDB client object using the provided URI, select a specific database, and references a particular collection within that database.

To design a user-friendly interface, I invested efforts in crafting the web application's structure, content, and interactivity by using HTML templates. 

By combining Flask for backend development, MongoDB Atlas for data storage, and HTML templates for frontend design, this web application stands as a solution for effective To-Do List management.