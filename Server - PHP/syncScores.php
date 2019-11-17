<?php
	// 
	// syncScores.php
	// Adds the user score to the database and returns the leaderboard
	//

	//Import global functions
	require('globalFunctions.php');

	//Get values
	$token = $_POST['token'];
	$score = $_POST['score'];
	$md5 = $_POST['md5'];
	
	if (isset($token) && isset($score) && isset($md5) && $token != "" && $score != "" && GetMD5Client($token . $score) == $md5) { 
		//Connect to the database
		$dbh = ConnectToDatabase();
		
		//Get the user token
		$query = $dbh->prepare('SELECT user_id, expires_at, token FROM mq_tokens WHERE status = 0;');
		$query->execute([$token]);
		$query->setFetchMode(\PDO::FETCH_ASSOC);
		$result = $query->fetchAll();
		
		//Check the token's credentials are correct
		$success = false;
		$id = 0;
		foreach($result as $r) {
            $tokenHash = $r['token'];
			if (password_verify($token, $tokenHash)) {
				$id = $r['user_id'];
				
				//Check the token has not expired
				if (new DateTime($r['expires_at']) <= new DateTime("now")) {
					$query = $dbh->prepare("UPDATE mq_users SET status = 1 WHERE id = ?;");
					$query->execute([$id]);
					
					$success = false;
				}
				else {
					$success = true;
				}
			}
        }
		//If the token is correct...
		if ($success) {
			//Add the score to the database
			$query = $dbh->prepare("INSERT INTO mq_scores (user_id, score, created_at) VALUES (?, ?, now());");
			$query->execute([$id, $score]);
			
			//Update the user highscore
			$query = $dbh->prepare("UPDATE mq_users SET highscore = ? WHERE id = ? AND highscore < ?;");
			$query->execute([$score, $id, $score]);
			
			//Get the leaderboard
			$query = $dbh->prepare("SELECT id, username, highscore FROM mq_users ORDER BY highscore DESC;");
			$query->execute();
			
			$query->setFetchMode(\PDO::FETCH_ASSOC);
			$result = $query->fetchAll();

			$newHighscore = false;
			$leaderboard = [];
			$player = [];
			$iteration = 0;
			$rank = 0;
			$lastScore = -1;
			
			$limit = 10;
			if (sizeof($result) < 10) {
				$limit = sizeof($result);
			}
			
			//For each result, get the highscore and username
			foreach ($result as $r) {
				if ($r['highscore'] > $lastScore) {
					$rank++;
					$lastScore = $r['highscore'];
				}
				if ($iteration < $limit) {
					array_push($leaderboard, [$rank, $r['username'], intval($r['highscore'])]);
				}
				
				if ($r['id'] == $id) {
					$player = [$rank, $r['username'], intval($r['highscore'])];
				}
				
				$iteration++;
				$rank++;
			}
			
			//Return the data
			$data = ["success" => "true",
					 "authenticated" => "true",
					 "leaderboard" => $leaderboard,
					 "player" => $player,
					 "md5" => GetMD5Server(json_encode([$leaderboard, $player]))];
			$json = json_encode($data);
			echo $json;
		}
		else {
			$data = ["success" => "true",
					 "authenticated" => "false"];
			$json = json_encode($data);
			echo $json;
		}
	}
	else {
		ReturnError("Invalid request");
	}

?>