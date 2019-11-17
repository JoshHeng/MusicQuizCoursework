<?php
	// 
	// attemptLogin.php
	// Attempts to log in the user and creates a token for the session
	//

	//Import global functions
	require('globalFunctions.php');
		
	//Get values
	$username = $_POST['username'];
	$password = $_POST['password'];
	$md5 = $_POST['md5'];

	if (isset($username) && isset($password) && isset($md5) && $username != "" && $password != "" && strlen($username) < 32 && strlen($password) < 256 && GetMD5Client($username . $password) == $md5) { 
		//Connect to the database
		$dbh = ConnectToDatabase();
		
		//Get the user details
		$query = $dbh->prepare('SELECT id, password, highscore, authorised FROM mq_users WHERE username = ?');
		$query->execute([$username]);
		$query->setFetchMode(\PDO::FETCH_ASSOC);
		$result = $query->fetchAll();
		
		//Check the password submited by the user
		$success = false;
		$id = 0;
		foreach($result as $r) {
            $passwordHash = $r['password'];
			if (password_verify($password, $passwordHash)) {
				$success = true;
				$id = $r['id'];
			}
        }
		
		//If password was correct, create a token for the user and return it
		if ($success) {
			$token = bin2hex(openssl_random_pseudo_bytes(64));
			$tokenHash = password_hash($token, PASSWORD_DEFAULT);
			$query = $dbh->prepare("INSERT INTO mq_tokens (user_id, token, created_at, expires_at) VALUES (?, ?, now(), DATE_ADD(now(), INTERVAL 1 DAY))");
			$query->execute([$id, $tokenHash]);
			
			$authorised = 'false';
			if ($r['authorised'] == 1) {
				$authorised = 'true';
			}
			
			$data = ["success" => "true",
					 "credentials" => "true",
					 "authorised" => $authorised,
					 "highscore" => $r['highscore'],
					 "token" => $token,
					 "md5" => GetMD5Server($username . $authorised . $r['highscore'] . $token)];
			$json = json_encode($data);
			echo $json;
		}
		else {
			$data = ["success" => "true",
					 "credentials" => 'false'];
			$json = json_encode($data);
			echo $json;
		}
	}
	else {
		ReturnError("Invalid request");
	}

?>