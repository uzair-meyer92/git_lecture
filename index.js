import mysql from 'mysql2/promise';
import express from 'express';
import { config } from 'dotenv';

config(); 

const pool = mysql.createPool({
    host: process.env.DB_HOSTNAME,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_DATABASE,
});

const app = express();
app.use(express.json());

app.listen(3030, () => {
    console.log('http://localhost:3030');
});

// Function to get all employees
const getEmployees = async () => {
    let [data] = await pool.query("SELECT * FROM employees");
    return data;
};

console.log(await getEmployees());


// Function to get a single employee by ID
const getEmployee = async (id) => {
    const [data] = await pool.query("SELECT * FROM employees WHERE id = ?", [id]);
    return data;
};

console.log(await getEmployee(1));

// Function to add a new employee
const addEmployee = async (name, salary, department_id) => {
    await pool.query("INSERT INTO employees (name, salary, department_id) VALUES (?, ?, ?)", [name, salary, department_id]);
    return await getEmployees(); // Return all employees after adding the new one
};

console.log(await addEmployee('John Doe', 50000, 1));

// Function to remove an employee by ID
const removeEmployee = async (id) => {
    await pool.query("DELETE FROM employees WHERE id = ?", [id]);
    return await getEmployees(); // Return all employees after removing the employee
};

console.log(await removeEmployee(1));

// Function to update an employee's details
const updateEmployee = async (id, name, salary, department_id) => {
    await pool.query("UPDATE employees SET name = ?, salary = ?, department_id = ? WHERE id = ?", [name, salary, department_id, id]);
    return await getEmployee(id); // Return the updated employee data
};

console.log(await updateEmployee(1, 'John Doe', 60000, 1));








