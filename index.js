import mysql from "mysql2/promise";
import {config} from "dotenv";
config();

const pool = mysql.createPool({
    hostname:process.env.HOSTNAME,
    user:process.env.USER,
    password:process.env.PASSWORD,
    database:process.env.DATABASE 
});


const app = express();
app.use(express.json());


app.listen(3000, () => {
    console.log('http://localhost:3000');
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

// Route to get all products
app.get('/products', async (req, res) => {
    const [rows] = await pool.query("SELECT * FROM products");
    res.json(rows);
});

// Route to get a single product by primary key (assuming product_code as primary key)
app.get('/products/:product_code', async (req, res) => {
    const { product_code } = req.params;
    const [rows] = await pool.query("SELECT * FROM products WHERE product_code = ?", [product_code]);
    res.json(rows[0] || {});
});

// Route to insert a new product
app.post('/products', async (req, res) => {
    const { product_code, product_name, product_price, product_quantity } = req.body;
    await pool.query(
        "INSERT INTO products (product_code, product_name, product_price, product_quantity) VALUES (?, ?, ?, ?)",
        [product_code, product_name, product_price, product_quantity]
    );
    res.status(201).json({ product_code });
});

// Route to delete a product by primary key
app.delete('/products/:product_code', async (req, res) => {
    const { product_code } = req.params;
    await pool.query("DELETE FROM products WHERE product_code = ?", [product_code]);
    res.status(200).send();
});

// Route to update a product by primary key
app.put('/products/:product_code', async (req, res) => {
    const { product_code } = req.params;
    const { product_name, product_price, product_quantity } = req.body;
    await pool.query(
        "UPDATE products SET product_name = ?, product_price = ?, product_quantity = ? WHERE product_code = ?",
        [product_name, product_price, product_quantity, product_code]
    );
    res.status(200).send();
});

// Route to get all users
app.get('/users', async (req, res) => {
    const [rows] = await pool.query("SELECT * FROM users");
    res.json(rows);
});

// Route to get a single user by primary key (assuming user_id as primary key)
app.get('/users/:user_id', async (req, res) => {
    const { user_id } = req.params;
    const [rows] = await pool.query("SELECT * FROM users WHERE user_id = ?", [user_id]);
    res.json(rows[0],{});
});

// Route to insert a new user
app.post('/users', async (req, res) => {
    const { username, email } = req.body;
    await pool.query("INSERT INTO users (username, email) VALUES (?, ?)", [username, email]);
    res.status(201).json({ username });
});

// Route to delete a user by primary key
app.delete('/users/:user_id', async (req, res) => {
    const { user_id } = req.params;
    await pool.query("DELETE FROM users WHERE user_id = ?", [user_id]);
    res.status(200).send();
});












