function initMap() {
    'use strict';

    // MAP CONFIG AND LOADING
    var map = new google.maps.Map(document.getElementById('company-map'), {
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

