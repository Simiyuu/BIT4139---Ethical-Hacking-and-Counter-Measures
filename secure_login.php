<?php

$host = '127.0.0.1';
$db   = 'secure_app';
$user = 'admin';
$pass = 'secure_password';

$pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);

$username = $_POST['username'];
$password = $_POST['password'];

$stmt = $pdo->prepare('SELECT * FROM users WHERE username = :username AND password = :password');

$stmt->execute(['username' => $username, 'password' => $password]);
$user = $stmt->fetch();

if ($user) {
    echo "Login successful.";
} else {
    echo "Invalid credentials.";
}
?>