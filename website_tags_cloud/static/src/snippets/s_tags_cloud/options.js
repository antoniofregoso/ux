odoo.define('website_tags_cloud.tags_cloud_editor', function (require) {
    'use strict';
    
    var sOptions = require('web_editor.snippets.options');
    var wUtils = require('website.utils');
    
    sOptions.registry.s_tags_cloud_select = sOptions.Class.extend({
    
        //--------------------------------------------------------------------------
        // Private
        //--------------------------------------------------------------------------
    
        /**
         * @override
         */
        _renderCustomXML: function (uiFragment) {
            return this._rpc({
                model: 'tags_cloud.tags_cloud',
                method: 'search_read',
                args: [wUtils.websiteDomain(this), ['name']],
            }).then(clouds => {
                const menuEl = uiFragment.querySelector('[name="cloud_selection"]');
                for (const cloud of clouds) {
                    const el = document.createElement('we-button');
                    el.dataset.selectDataAttribute = cloud.id;
                    el.textContent = cloud.name;
                    menuEl.appendChild(el);
                }
            });
        },
        
    });
    });