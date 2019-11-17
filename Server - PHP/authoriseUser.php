<?php
	// 
	// authoriseUser.php
	// Authorises the user in the database
	//

	//Import global functions
	require('globalFunctions.php');

	//Get values
	$username = $_POST['username'];
	$key = $_POST['key'];

	if (isset($username) && $username != "" && isset($key) && $key == "dasji21u98DAj2989fjsaFAu985ufASJFoj") { 
		//Connect to the database
		$dbh = ConnectToDatabase();
		
		//Set user
		$query = $dbh->prepare('UPDATE mq_users SET authorised = 1 WHERE username = ?;');
		$query->execute([$username]);

		$data = ["success" => "true"];
		$json = json_encode($data);
		echo $json;
	}
	else {
		ReturnError("Invalid request");
	}

?>