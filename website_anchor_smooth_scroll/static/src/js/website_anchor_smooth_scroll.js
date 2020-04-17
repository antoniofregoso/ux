/* Copyright 2016 Antiun Ingeniería S.L. - Jairo Llopis
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */
odoo.define('website_anchor_smooth_scroll.website_anchor_smooth_scroll', function (require) {

    "use strict";

  

    document.querySelectorAll$("a[href^='#']").forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
