/**
 * -----------------------------------------------------------------------------------------------
 * AUTHOR MENTION:
 * -----------------------------------------------------------------------------------------------
 *     This is a verbatim copy of an excerpt from the OCA <Web> module to which I have added more
 * colors to the buttons.
 * 
 * Original code:
 * <https://github.com/OCA/OCB/blob/12.0/addons/web/static/src/js/fields/basic_fields.js>
 * 
 * -----------------------------------------------------------------------------------------------
 * The contributors at the time of copying this code are 45, please consult them on the github link
 * -----------------------------------------------------------------------------------------------
*/
odoo.define('xestionsat_state_selection_plus.widget', function (require) {
    "use strict";
    
    /**
     * This module contains most of the basic (meaning: non relational) field
     * widgets. Field widgets are supposed to be used in views inheriting from
     * BasicView, so, they can work with the records obtained from a BasicModel.
     */
    
    var AbstractField = require('web.AbstractField');
    var core = require('web.core');
    var field_registry = require('web.field_registry');
    
    var qweb = core.qweb;
    
    var StateSelectionPlusWidget = AbstractField.extend({
        template: 'FormSelection',
        events: {
            'click .dropdown-item': '_setSelection',
        },
        supportedFieldTypes: ['selection'],

        //--------------------------------------------------------------------------
        // Private
        //--------------------------------------------------------------------------

        /**
         * Prepares the state values to be rendered using the FormSelection.Items template.
         *
         * @private
         */
        _prepareDropdownValues: function () {
            var self = this;
            var _data = [];
            var current_stage_id = self.recordData.stage_id && self.recordData.stage_id[0];
            var stage_data = {
                id: current_stage_id,
                legend_none: this.recordData.legend_none || undefined,
                legend_red : this.recordData.legend_red || undefined,
                legend_orange : this.recordData.legend_orange || undefined,
                legend_yellow : this.recordData.legend_yellow || undefined,
                legend_light_blue : this.recordData.legend_light_blue || undefined,
                legend_dark_purple : this.recordData.legend_dark_purple || undefined,
                legend_salmon_pink : this.recordData.legend_salmon_pink || undefined,
                legend_medium_blue : this.recordData.legend_medium_blue || undefined,
                legend_dark_blue : this.recordData.legend_dark_blue || undefined,
                legend_fushia : this.recordData.legend_fushia || undefined,
                legend_green: this.recordData.legend_green || undefined,
                legend_purple : this.recordData.legend_purple || undefined,
            };
            _.map(this.field.selection || [], function (selection_item) {
                var value = {
                    'name': selection_item[0],
                    'tooltip': selection_item[1],
                };
                if (selection_item[0] === 'none') {
                    value.state_class = 'oe_kanban_color_plus_0';
                    value.state_name = stage_data.legend_none ? stage_data.legend_none : selection_item[1];
                } else if (selection_item[0] === 'red') {
                    value.state_class = 'oe_kanban_color_plus_1';
                    value.state_name = stage_data.legend_red ? stage_data.legend_red : selection_item[1];
                } else if (selection_item[0] === 'orange') {
                    value.state_class = 'oe_kanban_color_plus_2';
                    value.state_name = stage_data.legend_orange ? stage_data.legend_orange : selection_item[1];
                } else if (selection_item[0] === 'yellow') {
                    value.state_class = 'oe_kanban_color_plus_3';
                    value.state_name = stage_data.legend_yellow ? stage_data.legend_yellow : selection_item[1];
                } else if (selection_item[0] === 'light_blue') {
                    value.state_class = 'oe_kanban_color_plus_4';
                    value.state_name = stage_data.legend_light_blue ? stage_data.legend_light_blue : selection_item[1];
                } else if (selection_item[0] === 'dark_purple') {
                    value.state_class = 'oe_kanban_color_plus_5';
                    value.state_name = stage_data.legend_dark_purple ? stage_data.legend_dark_purple : selection_item[1];
                } else if (selection_item[0] === 'salmon_pink') {
                    value.state_class = 'oe_kanban_color_plus_6';
                    value.state_name = stage_data.legend_salmon_pink ? stage_data.legend_salmon_pink : selection_item[1];
                } else if (selection_item[0] === 'medium_blue') {
                    value.state_class = 'oe_kanban_color_plus_7';
                    value.state_name = stage_data.legend_medium_blue ? stage_data.legend_medium_blue : selection_item[1];
                } else if (selection_item[0] === 'dark_blue') {
                    value.state_class = 'oe_kanban_color_plus_8';
                    value.state_name = stage_data.legend_dark_blue ? stage_data.legend_dark_blue : selection_item[1];
                } else if (selection_item[0] === 'fushia') {
                    value.state_class = 'oe_kanban_color_plus_9';
                    value.state_name = stage_data.legend_fushia ? stage_data.legend_fushia : selection_item[1];
                } else if (selection_item[0] === 'green') {
                    value.state_class = 'oe_kanban_color_plus_10';
                    value.state_name = stage_data.legend_green ? stage_data.legend_green : selection_item[1];
                } else if (selection_item[0] === 'purple') {
                    value.state_class = 'oe_kanban_color_plus_11';
                    value.state_name = stage_data.legend_purple ? stage_data.legend_purple : selection_item[1];
                } else {
                    value.state_class = 'oe_kanban_color_plus_8';
                    value.state_name = stage_data.legend_dark_blue ? stage_data.legend_dark_blue : selection_item[1];
                }
                _data.push(value);
            });
            return _data;
        },

        /**
         * This widget uses the FormSelection template but needs to customize it a bit.
         *
         * @private
         * @override
         */
        _render: function () {
            var self = this;
            var states = this._prepareDropdownValues();
            // Adapt "FormSelection"
            // Like priority, default on the first possible value if no value is given.
            var currentState = _.findWhere(states, {name: self.value}) || states[0];
            this.$('.o_status')
                .removeClass('oe_kanban_color_plus_0 oe_kanban_color_plus_1 oe_kanban_color_plus_2 oe_kanban_color_plus_3 oe_kanban_color_plus_4 oe_kanban_color_plus_5 oe_kanban_color_plus_6 oe_kanban_color_plus_7 oe_kanban_color_plus_8 oe_kanban_color_plus_9 oe_kanban_color_plus_10 oe_kanban_color_plus_11')
                .addClass(currentState.state_class)
                .prop('special_click', true)
                .parent().attr('title', currentState.state_name)
                .attr('aria-label', self.string + ": " + currentState.state_name);

            // Render "FormSelection.Items" and move it into "FormSelection"
            var $items = $(qweb.render('FormSelection.items', {
                states: _.without(states, currentState)
            }));
            var $dropdown = this.$('.dropdown-menu');
            $dropdown.children().remove(); // remove old items
            $items.appendTo($dropdown);
        },

        //--------------------------------------------------------------------------
        // Handlers
        //--------------------------------------------------------------------------

        /**
         * Intercepts the click on the FormSelection.Item to set the widget value.
         *
         * @private
         * @param {MouseEvent} ev
         */
        _setSelection: function (ev) {
            ev.preventDefault();
            var $item = $(ev.currentTarget);
            var value = String($item.data('value'));
            this._setValue(value);
            if (this.mode === 'edit') {
                this._render();
            }
        },
    });

    field_registry.add("state_selection_plus", StateSelectionPlusWidget);

    return StateSelectionPlusWidget;
    
});
