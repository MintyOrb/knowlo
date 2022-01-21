<template>
    <div> 
         <!-- image -->
    <div v-if='this.displayType=="image"'>
      <img class='imgg' :src="resource.url" />
    </div>
    <!--  youtube -->
    <div v-if='this.displayType=="embed"'>
      <div class="video-container ">
        <iframe :src="'https://youtube.com/embed/'+ytID+'?rel=0&autoplay=1'"  frameborder=”0″ allowfullscreen></iframe>
      </div>
    
      <!-- <vue-plyr>
        <div data-plyr-provider="youtube" :data-plyr-embed-id="resource.ytID"></div>
      </vue-plyr> -->

    </div>
    </div>
</template>
<script>
import { defineComponent } from 'vue'

export default defineComponent({
    name: 'resView',
    props: ['resource'],
    mounted () {
        this.determineResourceDisplay()
    },
    data () {
        return {
            ytID: '',
            displayType: ''
        }
    },
    methods: {
        determineResourceDisplay: function () {
            if (this.resource.url) {
                if (this.resource.url.match(/[^/]+(jpg|png|gif|jpeg)$/)) {
                    this.displayType = 'image'
                } else if (this.resource.url.match(/[^/]+(gifv|webm|mp4)$/)) {
                    this.displayType = 'video'
                } else if (this.resource.url.indexOf('youtube') > -1) {
                    this.ytID = new URL(this.resource.url).searchParams.get('v')
                    this.displayType = 'embed'
                }
            } else if (this.resource.hasOwnProperty('null')) { // not sure why it has the null prop to begin with...
                this.displayType = 'icon'
            } else {
                this.displayType = 'text'
            }
        }
    }
})
</script>
<style>
.imgg {
    max-width: 100%;
}
.web-container iframe, .video-container object, .video-container embed {
    position: absolute;
    top: 0;
    left: 0;
    width: 50%;
    height: 100%;
}
.video-container {
    position: relative;
    padding-bottom: 56.25%;
    padding-top: 30px;
    height: 0;
    overflow: hidden;
}
.video-container iframe, .video-container object, .video-container embed {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

</style>