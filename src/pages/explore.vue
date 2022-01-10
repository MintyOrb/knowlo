<template>
    <q-page>
        <splitpanes class="default-theme panes" :horizontal='horiz'>
            <pane size="50" class="rPane" :class="{ hideOverflow: collectionOptions.display == 'slider' }">
                
                <resource-display-options
                    @update-order="updateOrder"
                    @update-display="updateDisplay"
                    @update-size="updateSize"
                    @update-descending="updateDescending"
                ></resource-display-options>
                <resource-collection ref='collection' :resources="resources" :options="collectionOptions"></resource-collection>
                <q-btn @click.prevent="add">add</q-btn>
                <q-btn @click.prevent="horiz = !horiz">orientation</q-btn>
            </pane>
            <pane size="50" class="gPane">
                <q-btn @click.prevent="addg" style='z-index: 10'>addgg</q-btn>
                <graphNav :graph='network'></graphNav>   
            </pane>
        </splitpanes>
    </q-page>
</template>

<script>
import { defineComponent } from 'vue';
import graphNav from 'components/graphNav'
import { Splitpanes, Pane } from 'splitpanes'
import 'splitpanes/dist/splitpanes.css'
import resourceDisplayOptions from 'components/resourceDisplayOptions'
import resourceCollection from 'components/resourceCollection'

export default defineComponent({
    components: { Splitpanes, Pane, graphNav, resourceDisplayOptions, resourceCollection },
    data() {
        return {
            horiz: 'true',
            tagQuery: this.$q.localStorage.getItem('tagQuery') || [],
            resources: [
                {
                    title: 'hi',
                    text: 'test',
                    subtitle: 'ummmm',
                    uid: 1,
                    resource: {
                        mThumb: 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Operation_Upshot-Knothole_-_Badger_001.jpg/1058px-Operation_Upshot-Knothole_-_Badger_001.jpg',
                        uid: 1
                    }
                },
                {
                    title: 'hi',
                    text: 'test',
                    subtitle: 'ummmm',
                    uid: 1,
                    resource: {
                        mThumb: 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Operation_Upshot-Knothole_-_Badger_001.jpg/1058px-Operation_Upshot-Knothole_-_Badger_001.jpg',
                        uid: 3
                    }
                },
                {
                    title: 'hi',
                    text: 'test',
                    subtitle: 'ummmm',
                    uid: 1,
                    resource: {
                        mThumb: 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Operation_Upshot-Knothole_-_Badger_001.jpg/1058px-Operation_Upshot-Knothole_-_Badger_001.jpg',
                        uid: 4
                    }
                },
                {
                    title: 'hi',
                    text: 'test',
                    subtitle: 'ummmm',
                    uid: 1,
                    resource: {
                        mThumb: 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Operation_Upshot-Knothole_-_Badger_001.jpg/1058px-Operation_Upshot-Knothole_-_Badger_001.jpg',
                        uid: 5
                    }
                },
                {
                    title: 'hi',
                    text: 'test',
                    subtitle: 'ummmm',
                    uid: 1,
                    resource: {
                        mThumb: 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Operation_Upshot-Knothole_-_Badger_001.jpg/1058px-Operation_Upshot-Knothole_-_Badger_001.jpg',
                        uid: 6
                    }
                },
                {
                    title: 'hi',
                    text: 'test',
                    subtitle: 'ummmm',
                    uid: 1,
                    resource: {
                        mThumb: 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Operation_Upshot-Knothole_-_Badger_001.jpg/1058px-Operation_Upshot-Knothole_-_Badger_001.jpg',
                        uid: 7
                    }
                },
                {
                    title: 'hi',
                    text: 'test',
                    subtitle: 'ummmm',
                    uid: 1,
                    resource: {
                        mThumb: 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Operation_Upshot-Knothole_-_Badger_001.jpg/1058px-Operation_Upshot-Knothole_-_Badger_001.jpg',
                        uid: 8
                    }
                },
                {
                    title: 'hi',
                    text: 'test',
                    subtitle: 'ummmm',
                    uid: 1,
                    resource: {
                        mThumb: 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Operation_Upshot-Knothole_-_Badger_001.jpg/1058px-Operation_Upshot-Knothole_-_Badger_001.jpg',
                        uid: 9
                    }
                },
                {
                    title: 'two',
                    text: 'hi again',
                    uid: 2,
                    resource: {
                        uid: 2
                    }
                }
            ],
            resourceQueryOptions: {
                include: [],
                exclude: [],
                skip: 0,
                limit: 30, // base on resources per row and mobile v desktop (i.e. available screen real estate)?
                order: this.$q.localStorage.getItem('exploreOrder') || 'quality',
                descending: this.$q.localStorage.getItem('exploreDescending') || 'true'
            },
            infinite: false, // flag indicating if resources should be concatenated or replaced
            noMore: false, // flag for no more related resources
            collectionOptions:{
                order: this.$q.localStorage.getItem('exploreOrder') || 'Quality',
                display: this.$q.localStorage.getItem('exploreDisplay') || 'card',
                size: this.$q.localStorage.getItem('exploreSize') || 4,
                descending: this.$q.localStorage.getItem('exploreDescending') || 'true',
            },
            network: {
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
        }
    },
    methods: {
        addg(){
      let x=0
      while( x < 10 ){
        x+=1
        let num = this.network.nodes.length + 2
        this.network.nodes.push({
          id: num,  label: num.toString(),  shape: 'circle',
        })
      }
     
      // this.edges.push({
      //   from: 6, to: 8
      // })
    },
        add(){
            this.resources.push({
                    title: 'hi',
                    text: 'test',
                    subtitle: 'ummmm',
                    uid: this.resources.length+1,
                    resource: {
                        mThumb: 'https://nitrocdn.com/BzukxzxIDWSkBjOuXIuFVkjjEriFmqlw/assets/static/optimized/rev-540763a/wp-content/uploads/2020/02/Cell-structure-768x467.jpg',
                        uid:  this.resources.length+1
                    }
                })
        },
        updateDisplay(x){
            this.$q.localStorage.set('exploreDisplay', x)
            this.collectionOptions.display = x
        },
        updateOrder(x){
            this.$q.localStorage.set('exploreOrder', x)
            this.collectionOptions.order = x
            this.resourceQueryOptions.order = x
            if(!this.noMore){ 
                this.fetchResources()
            }
        },
        updateSize(size){
            this.collectionOptions.size = size
            this.$q.localStorage.set('exploreSize', size)
            
        },
        updateDescending(x){
            this.$q.localStorage.set('exploreDescending', x)
            this.collectionOptions.descending = x
            this.resourceQueryOptions.descending = x
            if(!this.noMore){ 
                this.fetchResources()
            }
        }   
    }
})
</script>

<style scoped>
    .panes {
        height: calc(100vh - 50px);
    }
    .gPane {
        position: relative; width: 100%; height: 100%;
    }
    .rPane {
        position: relative; width: 100%; height: 100%;
        overflow-y: scroll;
    }
    .iso div {
        height: 100px;
        width: 200px;
    }

    .hideOverflow {
        overflow: hidden;
    }
</style>