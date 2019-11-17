<?php
	// 
	// getSongs.php
	// Returns a list of songs scraped from the current charts website
	//

	//Import global functions
	require('globalFunctions.php');

	//Use curl to fetch the official charts website's content
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, "https://www.officialcharts.com/charts/singles-chart/");
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	$outputString = curl_exec($ch);
	curl_close($ch);

	//Filter the HTML to only the songs table
	$startPosition = strpos($outputString, '<table class="chart-positions">');
	$endPosition = strpos($outputString, '</table>');
	$outputString = substr($outputString, $startPosition, $endPosition - $startPosition);

	//For each row in the table...
	$outputArray = preg_split('/<tr/', $outputString);
	$songs = [];
	foreach ($outputArray as $line) {
		//If the row is a song...
		if ($line[0] == ">" && strpos($line, 'googletag') == 0) {
			//Get the song title
			$startPosition = strpos($line, '<div class="title">');
			$titleString = substr($line, $startPosition + strlen('<div class="title">'));
			$endPosition = strpos($titleString, '</div>');
			$titleString = substr($titleString, 0, $endPosition);
			$startPosition = strpos($titleString, '">');
			$endPosition = strpos($titleString, '</a>');
			$titleString = substr($titleString, $startPosition + strlen('">'), $endPosition - ($startPosition + strlen('">')));
			
			//Get the artist
			$startPosition = strpos($line, '<div class="artist">');
			$artistString = substr($line, $startPosition + strlen('<div class="artist">'));
			$endPosition = strpos($artistString, '</div>');
			$artistString = substr($artistString, 0, $endPosition);
			$startPosition = strpos($artistString, '">');
			$endPosition = strpos($artistString, '</a>');
			$artistString = substr($artistString, $startPosition + strlen('">'), $endPosition - ($startPosition + strlen('">')));
			
			//Add the song details into an array
			$song = [html_entity_decode($artistString), html_entity_decode($titleString)];
			
			//Add song to list if doesn't contain any swear words (asterisks)
			if (strpos($song[0], '*') == 0 && strpos($song[1], '*') == 0) {
				array_push($songs, $song);
			}
		}
	}

	//Shuffle songs list
	shuffle($songs);
	
	//Return data
	$data = ["success" => "true",
			 "songs" => $songs,
			 "md5" => GetMD5Server(json_encode($songs))];
	$json = json_encode($data);
	echo $json;
?>