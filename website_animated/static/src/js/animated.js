                        
                        odoo.define('website_animated.animated', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');

    publicWidget.registry.Animated = publicWidget.Widget.extend({
        selector: '#wrapwrap',

        start: function () {
            const _objs = document.querySelectorAll('[data-animated]');
            let options = { threshold: 0.5}
            var observer = new IntersectionObserver(function(entries) {
                entries.forEach(entry => {
                    let animation = 'animate__'.concat(entry.target.dataset.animated);
                    if (entry.intersectionRatio > 0) {
                        if(entry.target.dataset.repeat!=undefined){
                            entry.target.classList.add('animate__'.concat(entry.target.dataset.repeat));
                        }
                        if(entry.target.dataset.speed!=undefined){
                            entry.target.classList.add('animate__'.concat(entry.target.dataset.speed));
                        }
                    entry.target.classList.add('animate__animated',  animation);
                    } else {
                        entry.target.addEventListener('animationend', () => {
                            entry.target.classList.remove('animate__animated',  animation);
                            });
                        }
                    }, options);
                });
            _objs.forEach(obj => {
                observer.observe(obj);
            });
        },


    });
});
