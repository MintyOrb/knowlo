<template>
  <div class="flex flex-center g">
    <div class='testbs'>
      <q-btn @click="add">add</q-btn>
      <q-btn @click="fit">fit</q-btn>
      <q-btn @click="fit([3])">fit3</q-btn>
      <q-btn @click="size">size</q-btn>
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
        :nodes="nodes"
        :edges="edges"
        :options="options"
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
  components: {
    network
  },
  data() {
    return {
      nodes: [
        {id: 1,  label: 'circle',  shape: 'circle' },
        {id: 2,  label: 'ellipse', shape: 'ellipse'},
        {id: 3,  label: 'database',shape: 'database'},
        {id: 4,  label: 'box',     shape: 'box'    },
        {id: 5,  label: 'diamond', shape: 'diamond'},
        {id: 6,  label: 'dot',     shape: 'dot'},
        {id: 7,  label: 'square',  shape: 'square'},
        {id: 8,  label: 'triangle',shape: 'triangle'},
      ],
      edges: [
        {from: 1, to: 2},
        {from: 2, to: 3},
        {from: 2, to: 4},
        {from: 2, to: 5}, 
        {from: 5, to: 6},
        {from: 5, to: 7},
        {from: 6, to: 8}
      ],
      options: {
         nodes: {
          borderWidth: 4
         },
         edges: {
          color: 'lightgray'
        }
      }
    }
  },
  methods: {
    add(){
      let x=0
      while( x < 10 ){
        x+=1
        let num = this.nodes.length + 2
        this.nodes.push({
          id: num,  label: num.toString(),  shape: 'circle',
        })
      }
     
      // this.edges.push({
      //   from: 6, to: 8
      // })
    },
    fit(node){
    
      let options = {animation: true}
      if(Array.isArray(node)){
        options['nodes'] = node
      }
      this.$refs.network.fit(options)
    },
    size(){
      this.$refs.network.setSize("100%","100%")
    }
  }
})
</script>
<style scoped>
  .testbs {
    margin-bottom: -35px;
    z-index: 3;
  }
</style>