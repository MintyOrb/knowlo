<template>
  <div id='options'  class="selection shadow-3" :class="{ 'selection--hidden': !showNavbar }">
    <div class="row container">
				<!-- <span class="col items-start viewBtn" :class="{'fade': !showViewed}" ><i class="material-icons ">remove_red_eye</i>
          <q-tooltip :disable="!this.$q.localStorage.getItem('showToolTips')" :delay="500" :offset="[0, 5]">show / hide viewed resources</q-tooltip>
        </span> -->

        <!-- display options select -->
        <span>
          <q-btn class="viewBtn"  flat round @click.stop.prevent="display = 'list'"><i class="material-icons">view_list</i>
           <q-tooltip :disable="!$q.localStorage.getItem('showToolTips')" :delay="500" :offset="[0, 5]">List view</q-tooltip>
          </q-btn>
           <q-btn class="viewBtn"  flat round @click.stop.prevent="display = 'slider'"><i class="material-icons">view_array</i>
           <q-tooltip :disable="!this.$q.localStorage.getItem('showToolTips')" :delay="500" :offset="[0, 5]">Slider view</q-tooltip>
          </q-btn>
          <q-btn class="viewBtn" flat round  @click.stop.prevent="display = 'card'"><i class="material-icons">dashboard</i>
           <q-tooltip :disable="!this.$q.localStorage.getItem('showToolTips')" :delay="500" :offset="[0, 5]">Grid view</q-tooltip>
          </q-btn>
          <q-btn class="viewBtn" flat round  ><i class="material-icons">photo_size_select_large</i>
            <q-tooltip :disable="!this.$q.localStorage.getItem('showToolTips')" :delay="500" :offset="[0, 5]">Resize</q-tooltip>
            <q-popup-edit class="pop" v-model="sizePopup" cover >
              <q-slider class='sizeSlider' markers @mouseup.prevent="" v-model="size" :min="1" :max="20" :step="1" reverse />
              <!-- <q-btn round>hi</q-btn> -->
            </q-popup-edit>
          </q-btn>
        </span>

        <!-- order by -->
        <span class='col self-end order'>
          <span class="right orderby">
            <q-btn-dropdown auto-close color="primary" flat dropdown-icon="none">
              <template v-slot:label>
                  {{orderby}}
                  <q-tooltip :disable="!$q.localStorage.getItem('showToolTips')" :delay="500" :offset="[0, 5]">Order by ______</q-tooltip>
              </template> 
              <q-list>
                <q-item clickable @click.prevent="orderby = 'quality'">
                  <q-item-section >quality</q-item-section>
                </q-item>
                <q-item clickable @click.prevent="orderby = 'complexity'">
                  <q-item-section >complexity</q-item-section>
                </q-item>
                <q-item clickable @click.prevent="orderby = 'added'">
                  <q-item-section >date added</q-item-section>
                </q-item>
                <q-item clickable @click.prevent="orderby = 'votes'">
                  <q-item-section >votes</q-item-section>
                </q-item>
                <q-item clickable @click.prevent="orderby = 'views'">
                  <q-item-section >views</q-item-section>
                </q-item>
                <q-item disable @click.prevent="orderby = 'activity'">
                  <q-item-section >responses</q-item-section>
                </q-item>
                <q-item disable @click.prevent="orderby = 'time'">
                  <q-item-section >time to view</q-item-section>
                </q-item>
              </q-list>         
            </q-btn-dropdown>
              <q-btn flat round @click.prevent="descending == 'true'?descending = 'false' :descending = 'true'" class='viewBtn'>
                <i class="material-icons ascDec" :class="{'flipVert': descending == 'false' }">
                  sort
                  <q-tooltip :disable="!$q.localStorage.getItem('showToolTips')" :delay="500" :offset="[0, 5]">Ascending / Descending</q-tooltip>
                </i>
              </q-btn>
          </span>
        </span>
      </div>

      <!-- <div style="border-bottom:none;">
        <br/>
        <div class="row right quantity">
          <div>Showing {{resources.length}} of {{resourcesRelated}}</div>
          <div v-if='member.uid'><span v-if="showViewed">Including</span><span v-else>Excluding</span> {{resourcesViewed}} viewed</div>
        </div>
      </div> -->
  </div>
</template>

<script>
export default {
  data () {
    return {
      display: this.$q.localStorage.getItem('exploreDisplay') || "card",
      size: this.$q.localStorage.getItem('exploreSize') || 4,
      orderby: this.$q.localStorage.getItem('exploreOrder') || 'quality',
      descending: this.$q.localStorage.getItem('exploreDescending') || 'true',
      sizePopup: null,
      showViewed: true,
      showNavbar: true,
      lastScrollPosition: 0
    }
  },
  watch: {
    display(display) {
      this.$emit('update-display', display)
    },
    size(size) {
      this.$emit('update-size', size)
    },
    orderby(orderby) {
      this.$emit('update-order', orderby)
      this.orderNotification()
    },
    descending (descending){
      this.$emit('update-descending', descending)
      this.orderNotification()
    }
  },
  methods: {
    orderNotification() {
      this.$q.notify({
        message: 'Order by ' + this.orderby + ', ' + (this.descending == 'true'? 'high to low' : 'low to high'),
        timeout: 1500,
        position: 'bottom-left',
      })
    },
    onScroll(){ // functionality guided by https://medium.com/@Taha_Shashtari/hide-navbar-on-scroll-down-in-vue-fb85acbdddfe
      const currentScrollPosition = document.getElementById("options").offsetTop
      if (currentScrollPosition < 0) {
        return
      }
      if (Math.abs(currentScrollPosition - this.lastScrollPosition) < 60) {
        return
      }
      this.showNavbar = currentScrollPosition < this.lastScrollPosition
      this.lastScrollPosition = currentScrollPosition
    }
  },
  mounted () {
    document.getElementById("options").parentElement.addEventListener('scroll', this.onScroll)
  },
  beforeUnmount () {
    document.getElementById("options").parentElement.removeEventListener('scroll', this.onScroll)
  }


}
</script>

<style >
.pop {
    height: 28px;
    top: 46px;
    overflow: hidden;
}
/* hide progress bar on slider  */
.q-slider__track-container--h .q-slider__selection {
    visibility: hidden;
}
.q-item__section {
  text-transform: capitalize;
}
.q-btn__content {
  text-transform: capitalize;
}

.flipVert {
  transform: scaleY(-1);
}
.ascDec {
  transition: transform .5s;
}

/* is this going to overwrite the style everywhere in the app? It doesn't work when it the CSS is scoped */
.q-btn-dropdown__arrow-container {
  display: none!important;
}
.q-btn-dropdown {
  color: black!important;
}

.q-popup-edit {
  width: 70%;
}

.viewBtn{
  font-size: 20px;
}
.selection {
  top: 0px;
  background-color: white;
  position: sticky;
  z-index: 50;
  box-shadow: 0 2px 15px rgba(71, 120, 120, 0.5);
  transform: translate3d(0, 0, 0);
  transition: 0.1s all ease-out;
}
.selection.selection--hidden {
  box-shadow: none;
  transform: translate3d(0, -100%, 0);
}
</style>