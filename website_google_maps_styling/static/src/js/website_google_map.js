function initialize_map() {
    'use strict';

    // MAP CONFIG AND LOADING
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: {lat: mapLat, lng: mapLng},
        styles: mapTheme
    });

}

// Initialize map once the DOM has been loaded
google.maps.event.addDomListener(window, 'load', initialize_map);
