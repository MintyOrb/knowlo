<script>
import { defineComponent, h } from 'vue';
var _ = require("lodash"), Isotope = require("isotope-layout");
const prop = {
      options: {
        type: Object,
        default: {
          layoutMode: 'masonry',
          masonry: {
            gutter: 10
          }
        },
      },
      itemSelector: {
        type: String,
        default: "item"
      },
      list: {
        type: Array,
        required: true
      }
    }
export default defineComponent ({
    name: 'isotope',
    props: prop,
    data() {
        return {
            children: [],
            removedIndex: []
        }
    },
    render() {
        console.log(this.children)
        const map = {}
        const rawChildren = this.$slots.default || []
        const prevChildren = this.children
        // this.children = []
                console.log(this.children)

        const removedIndex = []

        // rawChildren.forEach(elt => addClass(elt, this.itemSelector))
        Array.prototype.forEach.call(rawChildren, elt => {
          addClass(elt, this.itemSelector)
        });

        for (let i = 0; i < rawChildren.length; i++) {
          const c = rawChildren[i]
          if (c.tag) {
            if (c.key != null && String(c.key).indexOf('__vlist') !== 0) {
              this.children.push(c)
              map[c.key] = c
                      console.log(this.children)

            } else {
              const opts = c.componentOptions
              const name = opts ? (opts.Ctor.options.name || opts.tag || '') : c.tag
              console.log(`Warning template error: isotope children must be keyed: <${name}>`)
            }
          }
        }

        const displayChildren = [...this.children]

        if (prevChildren) {
          for (let i = 0; i < prevChildren.length; i++) {
            const c = prevChildren[i]
            if (!map[c.key]) {
              displayChildren.splice(i, 0, c)
              removedIndex.push(i)
            }
          }
        }

        return h('div', null, displayChildren)
    },
    mounted() {
        const options = _.merge({}, this.compiledOptions)
        var update = (object) => {
          _.forOwn(object, (value, key) => {
            object[key] = (itemElement) => { const res = getItemVm(itemElement); return value.call(this, res.vm, res.index); };
          });
        };
        update(options.getSortData)
        update(options.getFilterData);
        this._isotopeOptions = options
        if (options.filter) {
          options.filter = this.buildFilterFunction(options.filter)
        }

        this.$nextTick(() => {       
          this.link()
          this.listen()
          console.log('new iso coming up')
          const iso = new Isotope(this.$el, options)
        console.log(iso)
          iso._requestUpdate = () => {
            if (iso._willUpdate)
              return

            iso._willUpdate = true
            this.$nextTick(() => {
              iso.arrange()
              iso._willUpdate = false
            });
          };
          this.iso = iso
        })
    },
    beforeUnmount() {
        _.forEach(this._listeners, (unlisten) => { unlisten(); })
        if (this._filterlistener) {
          this._filterlistener()
        }
        this.iso = null
    },
    beforeUpdate() {
        this._oldChidren = Array.prototype.slice.call(this.$el.children)
    },
    updated() {
        if (!this.iso) {
          return;
        }

        const newChildren = [...this.$el.children]
        const added = _.difference(newChildren, this._oldChidren)
        const removed = this.removedIndex.map(index => this.$el.children[index])

        this.cleanupNodes()
        this.link()

        if ((!removed.length) && (!added.length))
          return;

        this.listen()

        this.iso.remove(removed)
        this.iso.insert(added)
        this.iso._requestUpdate()
    },
    methods: {
        cleanupNodes() {
          this.removedIndex.reverse()
          this.removedIndex.forEach(index => this._vnode.children.splice(index, 1))
        },

        link() {
            const slots = this.$slots.default || []
            // slots.forEach(
            // (slot, index) => {
            //   const elmt = slot.elm
            //   if (elmt)
            //     elmt.__underlying_element = { vm: this.list[index], index }
            // })
            Array.prototype.forEach.call(slots, (slot, index) => {
                const elmt = slot.elm
                if (elmt)
                    elmt.__underlying_element = { vm: this.list[index], index }
            });
        },

        listen() {
          this._listeners = _(this.compiledOptions.getSortData).map((sort) => {
            return _.map(this.list, (collectionElement, index) => {
              return this.$watch(() => { return sort(collectionElement); }, () => {
                this.iso.updateSortData();
                this.iso._requestUpdate();
              });
            });
          }).flatten().value();
        },

        sort(name) {
          let sort = name
          if (_.isString(name)) {
            sort = { sortBy: name }
          }
          this.arrange(sort)
          this.$emit("sort", name)
        },

        buildFilterFunction (name) {
          const filter = this._isotopeOptions.getFilterData[name]
          this._filterlistener = this.$watch(() => { return _.map(this.list, (el, index) => this.options.getFilterData[name](el, index)); },
                                              () => { this.iso._requestUpdate(); });
          return filter
        },

        filter(name) {
          const filter = this.buildFilterFunction(name)
          this.arrange({ filter })
          this.$emit("filter", name)
        },

        unfilter() {
          this.arrange({ filter: () => { return true; } })
          this.$emit("filter", null)
        },

        layout(name) {
          let layout = name
          if (_.isString(name)) {
            layout = { layoutMode: name }
          }
          this.arrange(layout)
          this.$emit("layout", layout)
        },

        arrange(option) {
          this.iso.arrange(option)
          this.$emit("arrange", option)
        },

        shuffle() {
          this.iso.shuffle()
          this.$emit("shuffle")
          this.$emit("sort", null)
        },

        getFilteredItemElements() {
          return this.iso.getFilteredItemElements()
        },

        getElementItems() {
          return this.iso.getElementItems()
        }
    },
    computed: {
        compiledOptions() {
          const options = _.merge({}, this.options, { itemSelector: "." + this.itemSelector, isJQueryFiltering: false })

          _.forOwn(options.getSortData, (value, key) => {
            if (_.isString(value))
              options.getSortData[key] = (itemElement) => { return itemElement[value]; };
          });

          return options;
        }
    }
})

function addClass(node, classValue) {
    if (node.data) {
        const initValue = (!node.data.staticClass) ? "" : node.data.staticClass + " "
        node.data.staticClass = initValue + classValue
    }
}

function getItemVm(elmt) {
    return elmt.__underlying_element
}
</script>