function initMap() {
    'use strict';

    // MAP CONFIG AND LOADING
    
    var mapDiv = document.getElementById('company-map');
    var map = new google.maps.Map(mapDiv, {
        zoom: 12,
        center: {lat: mapLat, lng: mapLng},
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        styles: mapTheme
    });
}

google.maps.event.addDomListener(window, 'load', initMap);



