<?php

function from($datetime_object) {
    $gigasecond = '+1000000000 seconds';
    $gs = clone $datetime_object;
    $gs->modify($gigasecond);
    return $gs;
}
