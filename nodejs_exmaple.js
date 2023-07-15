const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const child_process = require('child_process');
const fs = require('fs');
const app = express();
app.use(express.json());

app.get('/r1', (req, res) => {
    let id = req.query.id;
    let db = new sqlite3.Database('./my_database.db');

    db.all(`SELECT * FROM users WHERE id = ${id}`, (err, row) => {
        res.send(row);
    });

    db.close();
});

app.get('/r2', (req, res) => {
    let id = req.query.id;
    let db = new sqlite3.Database('./my_database.db');

    db.all('SELECT * FROM users WHERE id = ?', id, (err, row) => {
        res.send(row);
    });

    db.close();
});

app.get('/r3', (req, res) => {
    let filename = req.query.filename;

    child_process.exec(`cat ${filename}`, (err, stdout, stderr) => {
        res.send(stdout);
    });
});

app.get('/r4', (req, res) => {
    let filename = req.query.filename;

    fs.readFile(filename, 'utf8', (err, data) => {
        if (err) {
            console.error(err);
            return;
        }
        res.send(data);
    });
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
