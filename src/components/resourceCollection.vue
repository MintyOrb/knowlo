<template>
    <div>
        <!-- slider view -->
        <cross-section v-if="options.display=='slider'" :items="resources">
            <resource v-for="res in resources"
                :size="options.size"
                :display="'card'"
                :key="res.resource.uid"
                :re="res"
            ></resource>  
        </cross-section>

        <!-- card and list view -->
        <iso v-else ref="resourceBin" :items="resources" >
            <resource v-for="res in resources"
                @imgLoaded='layout'
                :size="options.size"
                :display="options.display"
                :key="res.resource.uid"
                :re="res"
            ></resource>
        </iso>
    

    </div>
</template>

<script>

import resource from 'components/resource'
import crossSection from 'components/cross-section'
import iso from 'components/isotopeLayout'

export default {
    components: { resource, crossSection, iso },
    props: ['tagQuery', 'resources', 'options'],
    methods: {
        layout(){
            if(this.$refs.resourceBin){
                this.$refs.resourceBin.layout()
            }
        },
        getOptions() {
            return {
                sortAscending: false,
                getSortData: {
                    // quality: function(res) {
                    //     return res.globalVote.quality || 0
                    // },
                    // complexity: function(res) {
                    //     return res.globalVote.complexity || 0
                    // },
                    // added: function(res) {
                    //     return res.resource.dateAdded || 'unknown'
                    // },
                    votes: 'votes',
                    // views: function(res) {
                    //     return res.resource.viewCount || 'nan'
                    // },
                    // 'activity': function(res) {
                    //     return res. 
                    // },
                    // 'time': function(res) {
                    //     return res.
                    // },
                }
            }
        },
    }

}
</script>

<style>

</style>