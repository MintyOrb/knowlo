<template>
    <q-page>
        <timeline :items="titems" :groups="tgroups"></timeline>
        <splitpanes class="default-theme panes" :horizontal='horiz' @resized="layout" >
            <pane size="50" class="rPane" :class="{ hideOverflow: collectionOptions.display == 'slider' }">
                
                <resource-display-options
                    @update-order="updateOrder"
                    @update-display="updateDisplay"
                    @update-size="updateSize"
                    @update-descending="updateDescending"
                ></resource-display-options>
                <q-btn @click.prevent="add">add</q-btn>
                <q-btn @click.prevent="orient">orientation</q-btn>
                <resource-collection ref='collection' :resources="resources" :options="collectionOptions"></resource-collection>
                
            </pane>
            <pane size="50" class="gPane">
                <q-btn @click.prevent="addg" style='z-index: 10'>add 10</q-btn>
                <radial-menu ref='radialMenu'></radial-menu>
                <graphNav ref='graph' :graph='network' @node-selected="test"></graphNav>   
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
import timeline from 'components/vis-timeline'
import RadialMenu from 'components/RadialMenu'
import size from '../data/size.js'
let resources = require ('../data/resources.json')

export default defineComponent({
    components: { Splitpanes, Pane, graphNav, resourceDisplayOptions, resourceCollection, timeline, RadialMenu },
    mounted() {
        this.network.nodes = []
        this.network.nodes.push({
                    id: size['properties']['english'],
                    shape: "circularImage",
                    image: '',
                    brokenImage: '',
                    label: size['properties']['english'],
            })
        for (let x in size.properties.contains) {    
            this.network.nodes.push({
                    id: size['properties']['contains'][x]['properties']['english'],
                    title: size['properties']['contains'][x]['properties']['english'],
                    uid: size['properties']['contains'][x]['properties']['uid'],
                    shape: "circularImage",
                    image: size['properties']['contains'][x]['properties']['url'],
                    brokenImage: 'https://cdn0.iconfinder.com/data/icons/interface-set-vol-2/50/No_data_No_info_Missing-512.png',
                    label: size['properties']['contains'][x]['properties']['english'],
            })
            this.network.edges.push({
                from: size['properties']['contains'][x]['properties']['english'],
                to: 'Size'
            })
        }
        this.resources = []
        for (let x in resources){
            this.resources.push({
                uid: resources[x]['r']['properties']['uid'],
                resource: resources[x]['r']['properties']
            })
        }

    },
    data() {
        return {
            tgroups: [
			    {id: 'a1', content:'Group one'},
			    {id: 'a2', content:'Group two'},
			    {id: 'a3', content:'Group three'}
			],
			titems: [
			    {id: 1, content: 'item 1', start: '2014-04-20'},
                {id: 2, content: 'item 2', start: '2014-04-14'},
                {id: 3, content: 'item 3', start: '2014-04-18'},
                {id: 4, content: 'item 4', start: '2014-04-16', end: '2014-04-19'},
                {id: 5, content: 'item 5', start: '2014-04-25'},
                {id: 6, content: 'item 6', start: '2014-04-27', type: 'point'}
			],
            horiz: true,
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
        test(tag, position) {
            console.log(this.$refs.radialMenu)
            // this.$refs.radialMenu.style=`visibilityy:visible; position: absolute!important; z-index:3; top: ${position.y}px; left: ${position.x}px;`
                      

            // console.log(document.getElementsByClassName("radialMenu"))
            let dude = document.getElementsByClassName("menu")
            dude[0].style=`visibilityy:visible; position: absolute!important; z-index:3; top: ${position.y}px; left: ${position.x}px; padding:0px;`
            // this.$refs.radialMenu.style.top = position.y- + 'px'
            // this.$refs.radialMenu.style.left = position.x + 'px'
 this.$refs.radialMenu.expand()
            // for(let res in this.resources) {
            //     if (!(tag.nodes[0] in this.resources[res].tags)) { // if doesn't contain tag
            //         this.resources.splice(res,1) // index, how many
            //     }
            // }
            
        },
        orient() {
            this.horiz = !this.horiz
            this.$nextTick(function () {
                this.layout()
                this.$refs.graph.fit()
            })
        },
        layout(x){       
            this.$refs.collection.layout()
        },
        addg(){
            let x=0
            while( x < 10 ){
                x+=1
                let num = this.network.nodes.length + 2
                this.network.nodes.push({
                id: num,  label: num.toString(),  shape: 'circle',
                })
            }
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
            if (this.$q.localStorage.getItem('exploreDisplay') == 'slider'){
                this.collectionOptions.size = 2
            } else {
                this.collectionOptions.size = this.$q.localStorage.getItem('exploreDisplay')
            }
        },
        updateOrder(x){
            this.$q.localStorage.set('exploreOrder', x)
            this.collectionOptions.order = x
            this.resourceQueryOptions.order = x
            // if(!this.noMore){ 
            //     this.fetchResources()
            // }
        },
        updateSize(size){
            this.collectionOptions.size = size
            this.$q.localStorage.set('exploreSize', size)
            
        },
        updateDescending(x){
            this.$q.localStorage.set('exploreDescending', x)
            this.collectionOptions.descending = x
            this.resourceQueryOptions.descending = x
            // if(!this.noMore){ 
            //     this.fetchResources()
            // }
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