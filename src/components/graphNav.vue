<template>
  <div class="flex flex-center g">
    <div class='testbs'>
      <q-btn @click="fit">fit</q-btn>
      <q-btn @click="fit(['Physics'])">fit physics</q-btn>
      <!-- <q-btn @click="remove">remove</q-btn>
      <q-btn @click="reset">reset</q-btn>
      <q-btn @click="fit">fit</q-btn>
      <q-btn @click="getTop">getTop</q-btn>
      <q-btn @click="getTop">getTop</q-btn> -->
    </div>
     <!-- <search class ='col' exclude="" input-id="mainSearch" holder-text="Search" @select="test"></search>       -->
      <!-- <network ref="network" class='net'
        :nodes="nodes"
        :edges="edges"
        :options="options"
        @hold="hold"
        @select-node="choose"
      >
      </network> -->
      <network ref="network" class='net'
        :nodes="this.graph.nodes"
        :edges="this.graph.edges"
        :options="this.graph.options"
        @select-node="nodeSelected"
      >
      </network>   
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import network from 'components/vis-network';
import "vis-network/styles/vis-network.css";

export default defineComponent({
  name: 'graphNav',
  props: ['graph'],
  components: {
    network
  },
  data() {
    return {
    }
  },
  methods: {
    fit(node){
      let options = {animation: true}
      if(Array.isArray(node)){
        options['nodes'] = node
      }
      this.$refs.network.fit(options)
    },
    nodeSelected(node){
      let fullNode = this.$refs.network.getNode(node['nodes'][0])
      let canvasPosition = this.$refs.network.getPositions(node['nodes'][0])
      let DOMPosition = this.$refs.network.canvasToDom(canvasPosition[node['nodes'][0]])
      this.$emit('node-selected', fullNode, DOMPosition)
    }
  }
})
</script>
<style scoped>
  .testbs {
    margin-bottom: -35px;
    z-index: 3;
  }
  .net {
    position: absolute; top: 0px; right: 0px; bottom: 0px; left: 0px;
  }
  .splitpanes--vertical > .splitpanes__splitter:before {left: -30px;right: -30px;height: 100%;}
  .splitpanes--horizontal > .splitpanes__splitter:before {top: -30px;bottom: -30px;width: 100%;}
</style>