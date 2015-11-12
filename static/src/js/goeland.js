openerp.goeland = function (instance, local)
{
    var _t = instance.web._t;
        _lt = instance.web._lt;
    var QWeb = instance.web.qweb;
    var items = [];

    instance.link = instance.web.form.AbstractField.extend({
        template: "link",
        init: function (view, code) {
            this._super(view, code);
        },
        // The key part:
        render_value: function() {
            this.$el[0].src = this.get("value");
        }
    });

    instance.web.form.widgets.add('link', 'instance.link');

    instance.SortedList = instance.web.form.AbstractField.extend({
        //template: "SortedList",
        /*
        init: function (view, code) {
            this._super(view, code);
        },
        */
        init: function() {
            this._super.apply(this, arguments);
            this.set("value", "");
        },
        start: function() {
            this.on("change:effective_readonly", this, function() {
                this.display_field();
                this.render_value();
        });
            this.display_field();
            return this._super();
        },
        display_field: function() {
            var self = this;
            my_instance = new instance.web.Model('goeland.arbre_envracinaire')
                .query(['name'])
                .filter([['isactive', '=', true]])
                .limit(10)
                .all()
                .then(function (results){
                    _(results).each(function(item) {
                       _(items).push(item);
                    });
                });
            //items.push({ name: 'momo', sortorder: 10});
            //items.push({ name: 'jimi', sortorder: 20});
            self.$el.html(QWeb.render('List', {widget: this, items: items}));
        },
        render_value: function() {
            this.$("input").val("999");
        }
    });

    instance.web.form.widgets.add('SortedList', 'instance.SortedList');

    local.HomePage = instance.Widget.extend({
        start: function() {
            var products = new local.ProductsWidget(
                this, ["cpu", "mouse", "keyboard", "graphic card", "screen"], "#00FF00");
            products.appendTo(this.$el);
        },
    });

    local.ProductsWidget = instance.Widget.extend({
        template: "ProductsWidget",
        init: function(parent, products, color) {
            this._super(parent);
            this.products = products;
            this.color = color;
        },
    });

    instance.web.client_actions.add(
        'goeland.homepage', 'instance.goeland.HomePage');

}
