<!DOCTYPE html>
<html>
<body>
    <div>
        <h1>Student Information System</h1>
        <p>
            This project is a <strong>Student Information System</strong> developed as part of the <strong>CC151</strong> course. 
            It is designed to manage student, program, and college data efficiently. The system allows users to add, edit, delete, 
            and search for records in a user-friendly interface.
        </p>
        <h2>Features</h2>
<ul>
    <li><strong>Student Management:</strong> Add, edit, delete, and search student records. View detailed student information, including ID, name, gender, year level, and program code.</li>
    <li><strong>Program Management:</strong> Add, edit, delete, and search program records. Manage program details, including program code, program name, and affiliated college.</li>
    <li><strong>College Management:</strong> Add, edit, delete, and search college records. Manage college details, including college code and college name.</li>
    <li><strong>Search and Sort:</strong> Search records by various fields (e.g., student ID, program name, college code, etc.). Sort records by columns for easier navigation and organization.</li>
    <li><strong>Data Validation:</strong> Ensures valid input for student IDs, names, program codes, and other fields. Prevents duplicate entries and invalid data formats.</li>
    <li><strong>CSV Integration:</strong> Stores all data in CSV files (<code>Student.csv</code>, <code>Program.csv</code>, <code>College.csv</code>) for easy access and management. Automatically updates CSV files when records are added, edited, or deleted.</li>
</ul>
        <h2>Installation</h2>
        <p>To run this project locally, follow these steps:</p>
        <ol>
            <li>Clone the repository:</li>
            <pre><code>git clone https://github.com/SamHuertas/CCC151-SSIS-v1.git</code></pre>
            <li>Navigate to the project directory:</li>
            <pre><code>cd student-information-system</code></pre>
            <li>Install the required dependencies:</li>
            <pre><code>pip install PyQt6 PyQt6-tools</code></pre>
            <li>Run the application:</li>
            <pre><code>python main.py</code></pre>
        </ol>
        <h2>Usage</h2>
        <p>
            Once the application is running, you can:
        </p>
        <ul>
            <li>Add new students, programs, or colleges using the respective forms.</li>
            <li>Edit or delete existing records by selecting them in the table.</li>
            <li>Search for specific records using the search bar.</li>
            <li>Sort records by using the dropdown menu.</li>
        </ul>
        <h2>License</h2>
        <p>
            Developed by Sam Alexis Huertas as part of CC151 for education purposes only.
        </p>
    </div>
</body>
</html>
