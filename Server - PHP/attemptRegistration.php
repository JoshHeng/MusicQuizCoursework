<?php
	// 
	// attemptRegistration.php
	// Registers a user
	//

	//Import global functions
	require('globalFunctions.php');

	//Get POST values
	$username = $_POST['username'];
	$password = $_POST['password'];
	$md5 = $_POST['md5'];

	//Check all the values in the requests met the required criteria
	if (isset($username) && isset($password) && isset($md5) && $username != "" && $password != "" && sizeof($username) < 32 && sizeof($password) < 256 && GetMD5Client($username . $password) == $md5) {
		if (preg_match("/[^a-zA-Z0-9]/", $username)) {
			ReturnError("Invalid username");
		}
		else {
			//Connect to the database
			$dbh = ConnectToDatabase();

			//See if the username already exists
			$query = $dbh->prepare('SELECT * FROM mq_users WHERE username = ?');
			$query->execute([$username]);
			$query->setFetchMode(\PDO::FETCH_ASSOC);
			$result = $query->fetchAll();

			if (sizeof($result) > 0) {
				ReturnError("Username already exists");
			}
			else {
				//Add the user into the database
				$password = password_hash($password, PASSWORD_DEFAULT);

				$query = $dbh->prepare("INSERT INTO mq_users (username, password, created_at) VALUES (?, ?, now())");
				$query->execute([$username, $password]);

				$data = ["success" => 'true'];
				$json = json_encode($data);
				echo $json;
			}
		}
	}
	else {
		ReturnError("Invalid request");
	}

?>