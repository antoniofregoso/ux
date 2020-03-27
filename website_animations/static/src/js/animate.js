odoo.define('website_animations.animate', function (require) {
'use strict';

var publicWidget = require('web.public.widget');

publicWidget.registry.Animated = publicWidget.Widget.extend({
	selector: '#wrapwrap',

    start: function () {
    	const _objs = document.querySelectorAll('[data-animated]');
    	var observer = new IntersectionObserver(function(entries) {
    		entries.forEach(entry => {
    			var animation = entry.target.dataset.animated;
    			if (entry.intersectionRatio > 0) {
    				entry.target.classList.add('animated',  animation);
    			} else {
    				entry.target.classList.remove('animated',  animation);
    				}
    			});
    		});
    	_objs.forEach(obj => {
			observer.observe(obj);
    	});
    },
	});

});

