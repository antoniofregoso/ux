odoo.define('website_tags_cloud.tags_cloud_editor', function (require) {
'use strict';

var core = require('web.core');
var sOptions = require('web_editor.snippets.options');
var wUtils = require('website.utils');

var _t = core._t;

sOptions.registry.s_tags_cloud_select = sOptions.Class.extend({
    /**
     * @override
     */
    start: function () {
        var def = this._rpc({
            model: 'tags_cloud.tags_cloud',
            method: 'search_read',
            args: [wUtils.websiteDomain(this), ['name']],
        }).then(clouds => {
            var allCloudsEl = this.el.querySelector('[data-filter-by-cloud-id="0"]');
            var menuEl = allCloudsEl.parentNode;
            for (const cloud of clouds) {
            	let el = allCloudsEl.cloneNode();
                el.dataset.filterByCloudId = cloud.id;
                el.textContent = cloud.name;
                menuEl.appendChild(el);
            }
            this._setActive();
        });

        return Promise.all([this._super.apply(this, arguments), def]);
    },
    
    
    /**
     * @see this.selectClass for parameters
     */
    filterByCloudId: function (previewMode, value, $opt) {
        value = parseInt(value);
        this.$target.attr('data-filter-by-cloud-id', value).data('filterByCloudId', value);
        this.trigger_up('widgets_start_request', {
            editableMode: true,
            $target: this.$target,
        });
    },

    _setActive: function () {
        this._super.apply(this, arguments);

        var activeCloudId = this.$target.data('filterByCloudId') || 0;

        this.$el.find('[data-filter-by-cloud-id]').removeClass('active');
        this.$el.find('[data-filter-by-cloud-id=' + activeCloudId + ']').addClass('active');
    },
	
});

});