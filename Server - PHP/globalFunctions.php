<?php
	// 
	// Provides global functions used by other API endpoints
	//

	//Get database credentials
	require('databaseCredentials.php');

	//MD5 functions which ensure the requests are not tamperered with
	function GetMD5Client($string) {
		$hash = md5($string . "asjioj9821u9j0faslf0921irasf" . $string[2] . strtoupper($string[0]) . "amko!98");
		return $hash;
	}
	function GetMD5Server($string) {
		$hash = md5($string . "3s14109dlf" . strtolower($string[2]) . "asjdo");
		return $hash;
	}

	//Return a JSON error
	function ReturnError($error) {
		$data = ["success" => "false",
				 "error" => $error];
		$json = json_encode($data);

		echo $json;
		die();
	}
	
	//Create a connection to the database
	function ConnectToDatabase() {
		global $db_hostname, $db_username, $db_password, $db_database;
		
		try {
			//Try to connect, otherwise return an error
			$dbh = new PDO('mysql:host='. $db_hostname .';dbname='. $db_database, $db_username, $db_password);
			return $dbh;
		} catch(PDOException $e) {
			ReturnError("A database error has occured");
		}
	}
?>