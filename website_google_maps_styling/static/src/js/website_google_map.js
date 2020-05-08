function initMap() {
    'use strict';

    // MAP CONFIG AND LOADING

    alert(mapLng);
    var map = new google.maps.Map(document.getElementById('company-map'), {
        zoom: 12,
        center: {lat: mapLat, lng: mapLng},
        styles: mapTheme
    });
}

google.maps.event.addDomListener(window, 'load', initMap);



