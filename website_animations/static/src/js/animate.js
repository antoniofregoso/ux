odoo.define('website_animations.animate', function (require) {
'use strict';

var publicWidget = require('web.public.widget');

publicWidget.registry.Animated = publicWidget.Widget.extend({
	selector: '#wrapwrap',

    start: function () {
    	const _objs = document.querySelectorAll('.animated');
    	var observer = new IntersectionObserver(function(entries) {
    		entries.forEach(entry => {
    		    if (entry.intersectionRatio > 0) {
    		      var animation =  entry.target.dataset.animation;
    		      entry.target.classList.add(animation, 'delay-1s', 'bounceIn');
    		    } else {
    		      entry.target.classList.remove(animation, 'delay-1s');
    		    }
    		  });
    		});
    	_objs.forEach(obj => {
			observer.observe(obj);
    	});
    },
	});

});

