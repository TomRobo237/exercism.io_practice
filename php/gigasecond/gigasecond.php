<?php

$GIGASECOND = new DateInterval('PT1000000000S');

function from($datetime_object) {
    global $GIGASECOND;
    $gs = clone $datetime_object;
    $gs->add($GIGASECOND);
    return $gs;
}
