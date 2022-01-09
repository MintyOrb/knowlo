<template>
    <q-page>
        <splitpanes class="default-theme panes" horizontal>
            <pane size="50">
                <resource-display-options
                    @update-order="updateOrder"
                    @update-display="updateDisplay"
                    @update-size="updateSize"
                    @update-descending="updateDescending"
                ></resource-display-options> 
                <resource-collection ref='collection' :resources="resources" :options="collectionOptions"></resource-collection>
                <template v-slot:loading>
                    <div class="row justify-center q-my-md">
                        <q-spinner color="primary" size="40px" />
                    </div>
                </template>
            </pane>
            <pane size="50" class="gPane">
                <graphNav ></graphNav>   
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
            tagQuery: this.$q.localStorage.getItem('tagQuery') || [],
            resources: [],
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
</style>