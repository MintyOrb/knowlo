<template>
    <div >
    <div class='bin' >
        <slot />
    </div>
    </div>
</template>
<script>
import { defineComponent } from 'vue';

var Isotope = require("isotope-layout");
export default defineComponent ({
    props: ['items'],
    name: 'iso',
    mounted() {
        this.iso = new Isotope( '.bin', {
            layoutMode: 'masonry',
            gutter: 10
        });
        this.$nextTick(function () {
            this.layout('masonry')
        })
    },
    updated() {
        this.iso.reloadItems()
        this.layout('masonry')
    },
    methods: {
        layout(name) {
          let layout = name
          if (name) {
            layout = { layoutMode: name }
          }
          if (this.iso){
              this.iso.arrange(layout)
            this.$emit("layout", layout)
          }
        }        
    },
    watch: {
        options: {
            deep: true,
            handler(a, b) {
                console.log(a,b)
               this.layout()
            }
        }
    }
})
</script>