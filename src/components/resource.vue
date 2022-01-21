<template>
  <div class='resource' :style="{ width: width }" :id="re.resource.uid" @mouseenter="hovering = true" @mouseleave="hovering = false"
		:class="{ 'listFullWidth': display=='list', 'list z-depth-1 hoverable': display === 'list', 'card z-depth-1 hoverable': display === 'card'}"
		>

    <q-dialog
      v-model="pop"
    >
      <q-card style="width: 700px; max-width: 80vw;">
        
        <resView :resource='re.resource'></resView>

        <q-card-actions align="right" class="bg-white text-teal">
          <q-btn flat label="X" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>

		<div v-if="re.resource.mThumb"
			:class="{
      'thumb waves-effect waves-block waves-light z-depth-1 hoverable': display==='thumb' || display =='list' || display === 'godMode', 'card-image': display==='card', 'list-image': display==='list', 'margin20': display==='thumb' || display==='list' , 'inline mb': display==='list'}"
			>
			<span @click='pop = true' :to="{ name: 'r'}">
				<img :src="re.resource.mThumb" @load="loaded" />
			</span>
		</div>
		<router-link @click='selected' v-if="re.resource.text && re.resource.text.length > 0 && display =='thumb'" :to="{ name: 'r'}">
			<div class="margin20 hoverable thumb">
				<span >{{re.resource.text.substring(0,5)}}...</span>
			</div>
		</router-link>
		<div class="rText"  v-if="!editing && (re.resource.text && display !='thumb') && (!re.resource.title || display ==='card')"
    :class="{
    'titleText truncate': display === 'list' && $route.name != 'tag'}"
    >
			<router-link @click='selected' :to="{ name: 'r'}">
				{{re.resource.text.substring(0,300)}}
			</router-link>
		</div>
  </div>
</template>

<script>
// import $ from 'jquery'
// import addResource from '@/components/addResource'
import resView from 'components/resView'
export default {
  name: 'resourceComponent',
  components: { resView },
  props: {
    re: Object,
    display: String,
    size: Number,
  },
  data: () => {
    return {
      pop: false,
      editing: false,
      width: 'calc(25% - 10px)',
      hovering: false,
      displayQuality: 0,
      displayComplexity: 0,
      ratingDisplay: ''
    }
  },
  methods: {
    loaded(x){
      this.$emit('imgLoaded')
    },
    voteLabel () {
      // can be html...
      return '<span><span class="left" style="color:orange">Q: ' + this.displayQuality.toString().substring(0, 4) + '</span> <span style="float:right; color:blue" class="">C: ' + this.displayComplexity.toString().substring(0, 4) + '</span></span>'
    },
    qualityChange (val) {
      if (!this.re.memberVote) {
        // this.re.memberVote = {}
      }
      if (val !== this.re.memberVote.quality) {
        // this.re.memberVote.quality = val
        this.vote()
      }
    },
    complexityChange (val) {
      if (!this.re.memberVote) {
        // this.re.memberVote = {}
      }
      if (!this.re.memberVote || val !== this.re.memberVote.complexity) {
        // this.re.memberVote.complexity = val
        this.vote()
      }
    },
    selected () {
      this.$emit('selected')
    },
    vote () {
      this.$http.put('/api/auth/resource/' + this.re.resource.uid + '/vote', {vote: this.re.memberVote}).then(response => {
        if (response.data) {
          // Materialize.toast('voted!', 2000)
          // this.re.globalVote = response.data.globalVote
          // this.re.votes = response.data.votes
          this.$emit('vote-cast')
          this.ratingDisplay = 'member'
        } else {
          // Materialize.toast('Something went wrong...', 4000)
        }
      }, response => {
        if (response.status === 401) {
          // Materialize.toast('You must be logged in to vote!', 4000)
          $('#login-modal').modal('open')
          this.ratingDisplay = 'global'
        } else {
          // Materialize.toast('Something went wrong...are you online?', 4000)
        }
      })
    },
    deleteResource (uid) {
      this.$http.delete('/api/auth/resource/' + uid + '/full').then(response => {
        if (response.data) {
          // Materialize.toast('deleted resource', 4000)
        } else {
          // Materialize.toast('Something went wrong...', 4000)
        }
      }, response => {
        // Materialize.toast('Something went wrong...are you online?', 4000)
      })
    },
    trimNumber (num, digits) { // from http://stackoverflow.com/a/9462382/2061741 - displays number of views
      if (num && digits && typeof (num) === 'number') {
        var si = [{ value: 1E18, symbol: 'E' }, { value: 1E15, symbol: 'P' }, { value: 1E12, symbol: 'T' }, { value: 1E9, symbol: 'G' }, { value: 1E6, symbol: 'M' }, { value: 1E3, symbol: 'k' }]
        var rx = /\.0+$|(\.[0-9]*[1-9])0+$/
        var i
        for (i = 0; i < si.length; i++) {
          if (num >= si[i].value) {
            return (num / si[i].value).toFixed(digits).replace(rx, '$1') + si[i].symbol
          }
        }
        return num.toFixed(digits).replace(rx, '$1')
      }
    },
    setSize(){
      if(this.display == 'card'){
        this.width = "calc(" + (1/this.size)*100 + "% - 10px)"
      }
    }
  },
  mounted () {
    this.setSize()
    this.ratingDisplay = 'global'
    if (this.re.editing) { // adding / editing resource
      this.editing = true
    }
  },
  watch: {
     size (x) {
      this.setSize()
    },
    ratingDisplay (val) {
      // if (val === 'global') {
      //   this.re.globalVote && this.re.globalVote.quality !== null ? this.displayQuality = this.re.globalVote.quality : this.displayQuality = 0
      //   this.re.globalVote && this.re.globalVote.complexity !== null ? this.displayComplexity = this.re.globalVote.complexity : this.displayComplexity = 0
      // } else {
      //   this.re.memberVote && this.re.memberVote.quality !== null ? this.displayQuality = this.re.memberVote.quality : this.displayQuality = 0
      //   this.re.memberVote && this.re.memberVote.complexity !== null ? this.displayComplexity = this.re.memberVote.complexity : this.displayComplexity = 0
      // }
    }
  },
  filters: {
    strr (val) {
      if (val === null) return 'n/a'
      return val.toString().substring(0, 4)
    },
    numm (val) {
      if (val === null) return 0
      return val
    }
  }
}
</script>

<style scoped>

.hoverable {
  box-shadow: none!important;
}
.hoverable:hover {
  box-shadow: 0 8px 17px 0 rgba(0,0,0,.2), 0 6px 20px 0 rgba(0,0,0,.19)!important;
}
.q-slider {
  margin-left: 7px;
  margin-right: 7px;
}
.vote {
  padding-left: 5px;
  padding-right: 5px;
}
.vote i {
  margin: 2px;
}
.list .thumb {
  margin:5px;
  border-radius: 0;
  height: 50px;
  width: 50px;
  overflow: hidden;
}
.voteView {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.resource a {color:black;}
.resource {
  /* max-height: 100%; */
}
.listFullWidth {
  width: 100%!important;
  margin-left: 0%!important;
}
.list span {
  font-size: 15px;
}
.list {
    outline: 1px solid #80808038;
    background-color: white;
    padding: .5% 1% 1% 2%;
    width: 94%;
    margin-left: 3%;
    min-height: 40px;
    font-size: 20px;
    display: flex;
    justify-content: flex-start;
    flex-flow: row wrap;
    align-items: center;
    max-width: 100vw;
}
.list:hover {
  z-index: 20;
}
.list-image img {
  max-height: 100%;
}
.card {
		box-shadow: none!important;
    margin: 5px!important;
    padding: 0px!important;
}
.card .card-image {
  max-height: 400px!important;
  overflow: hidden!important;
  margin-bottom: 10px;
}
.card-bottom {
    margin: -11px!important;
}
.card-bottom i {
    vertical-align: middle!important;
    margin-bottom: 3px!important;
    padding-left: 3px!important;
    padding-right: 3px!important;
}
.card .card-content {
    padding-bottom: 3px!important;
    padding-top: 14px!important;
}
.card .card-action {
		border-top: none!important;
}
.list .rText {
  font-size: 18px;
}
.title {
    font-size: 18px;
    font-weight: bold;
    line-height: .1;
}
.mb{
  margin-bottom: 12px;
}
.subtitle {
  font-size:14px;
}
.rText{
  font-size: 15px;
  font-weight: 300;
  padding:20px;
  white-space: pre-line;
  padding-top: 0;
}
.rating{
  opacity: .4;
  transition: opacity .5s;
}
.rating:hover{
  opacity: 1;
}
.rating.selected {
  opacity: 1;
}
.voteHalf {
  width: 50%;
  margin-left: auto;
}
.titleText {
  max-width: calc(50% - 110px)
}
  /* iPads (portrait and landscape) ----------- */
@media only screen
and (min-width : 768px)
and (max-width : 1024px) {
  /* .card{
    width: calc(25% - 10px)!important;
  } */
  .list {
    margin-left: 0;
    width: 100%;
  }
}
/* Desktops and laptops ----------- */
@media only screen
and (min-width : 1224px) {
  /* .card{
    width: calc(20% - 10px)!important;
  } */
}
_:-moz-tree-row(hover), .card {
    width: calc(20% - 15px)!important;
}
@media only screen
and (max-width : 375px) {
  /* .card{
    width: calc(100% - 10px)!important;
  } */
  .voteHalf {
    width: 100%;
    display: block;
    float: right;
  }
  .list {
    margin-left: 0;
    width: 100%;
  }
  .titleText {
    max-width: calc(100% - 110px);
  }
}
/* Smartphones (landscape) ----------- */
@media only screen
and (min-width : 376px)
and (max-width : 767px) {
  /* .card{
    width: calc(50% - 10px)!important;
  } */
  .voteHalf {
    width: 100%;
    display: block;
  }
  .list {
    margin-left: 0;
    width: 100%;
  }
.listFullWidth {
  width: 100%!important;
  margin-left: 0%!important;
}
  .titleText {
    max-width: calc(100% - 110px);
  }
}

</style>
