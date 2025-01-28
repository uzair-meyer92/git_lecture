import mysql from "mysql2/promise";
import {config} from "dotenv";
config();

const pool = mysql.createPool({
    hostname:process.env.HOSTNAME,
    user:process.env.USER,
    password:process.env.PASSWORD,
    database:process.env.DATABASE 
});


const getAllUsers = async () => {
    const [rows] = await pool.query("SELECT * FROM users");
    return rows;
}

console.log(await getAllUsers());


const getAllProducts = async () => {
    const [rows] = await pool.query("SELECT * FROM products");
    return rows;
}

console.log(await getAllProducts());


const deleteProduct = async () => {
    const [rows] = await pool.query("DELETE FROM products WHERE product_code = 'baro1'");
    return rows;
}

console.log(await deleteProduct());


const insertProduct = async () => {
    const [rows] = await pool.query("INSERT INTO products (product_code, product_name, product_price, product_quantity) VALUES ('baro1', 'baro', '10.00', '10')");
    return rows;
}

console.log(await insertProduct());


const updateProduct = async () => {
    const [rows] = await pool.query("UPDATE products SET product_price = '20.00' WHERE product_code = 'baro1'");
    return rows;
}

console.log(await updateProduct());




