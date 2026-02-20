<?php

// Read number of test cases
$t = intval(trim(fgets(STDIN)));

for ($i = 0; $i < $t; $i++) {
    // Read X and Y
    $line = trim(fgets(STDIN));
    $arr = explode(" ", $line);

    $x = intval($arr[0]);
    $y = intval($arr[1]);

    // Check if turn is good
    if (($x + $y) > 6) {
        echo "YES\n";
    } else {
        echo "NO\n";
    }
}

?>