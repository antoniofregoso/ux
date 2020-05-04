function initMap() {
    'use strict';

    // MAP CONFIG AND LOADING
    
    var mapDiv = document.getElementById('company-map');
    
    var map = new google.maps.Map(mapDiv, {
        zoom: 12,
        center: {lat: mapLat, lng: mapLng},
        styles: mapTheme
    });
    
    google.maps.event.addDomListener(mapDiv, 'click', function() {
        window.alert('Map was clicked!');
      });

    

}

document.addEventListener('readystatechange', event => {
	  if (event.target.readyState === 'interactive') {
	    //
	  }
	  else if (event.target.readyState === 'complete') {
	    initMap();
	  }
	});

