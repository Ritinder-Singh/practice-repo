<?php
declare(strict_types=1);
// PROJECT: Slim 4 REST API | composer require slim/slim slim/psr7 && php -S localhost:8080 index.php
// Docs: https://www.slimframework.com/docs/v4/

// TODO 1: Bootstrap Slim
//   require __DIR__ . '/vendor/autoload.php';
//   use Slim\Factory\AppFactory;
//   use Psr\Http\Message\ServerRequestInterface as Request;
//   use Psr\Http\Message\ResponseInterface as Response;
//   $app = AppFactory::create();
//   $app->addBodyParsingMiddleware();
//   $app->addErrorMiddleware(true, true, true);

// TODO 2: In-memory user store
//   $users = [
//       ["id" => 1, "name" => "Alice", "email" => "alice@example.com"],
//       ["id" => 2, "name" => "Bob",   "email" => "bob@example.com"],
//   ];

// TODO 3: GET /users
//   $app->get('/users', function(Request $req, Response $res) use (&$users): Response {
//       $res->getBody()->write(json_encode($users));
//       return $res->withHeader('Content-Type', 'application/json');
//   });

// TODO 4: GET /users/{id}
//   $app->get('/users/{id}', function(Request $req, Response $res, array $args) use (&$users): Response {
//       $user = array_values(array_filter($users, fn($u) => $u['id'] === (int)$args['id']))[0] ?? null;
//       if (!$user) return $res->withStatus(404)->withHeader('Content-Type', 'application/json');
//       $res->getBody()->write(json_encode($user));
//       return $res->withHeader('Content-Type', 'application/json');
//   });

// TODO 5: POST /users — parse JSON body, validate, create
// TODO 6: PUT /users/{id} — update user
// TODO 7: DELETE /users/{id} — remove, return 204

// TODO 8: Add PDO middleware for SQLite persistence
//   $db = new PDO("sqlite:users.db");
//   $db->exec("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL)");
//   // Replace in-memory array with PDO queries

// $app->run();
echo "TODO: run composer install, then uncomment app setup";
