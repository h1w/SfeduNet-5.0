<template>
    <div style="height: 900px; width: 100%">
        <l-map
        v-if="showMap"
        :zoom="zoom"
        :center="center"
        :options="mapOptions"
        style="height: 80%"
        @update:center="centerUpdate"
        @update:zoom="zoomUpdate"
        >
            <l-tile-layer :url="url" :attribution="attribution" />
            <Vue2LeafletHeatmap :lat-lng="latlngs" :radius="25" :min-opacity=".75" :max-zoom="10" :blur="25"></Vue2LeafletHeatmap>
        </l-map>
    </div>
</template>

<script>
import { latLng, icon } from 'leaflet'
import { LMap, LTileLayer } from "vue2-leaflet"
import Vue2LeafletHeatmap from './Vue2LeafletHeatmap.vue'
import axios from 'axios'

export default {
    name: 'HeatMap',
    components: {
        LMap,
        LTileLayer,
        Vue2LeafletHeatmap
    },
    data() {
        return {
            zoom: 12,
            center: latLng(47.2243657, 38.9105216),
            url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            // attribution: '<a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            // withPopup: latLng(47.41322, -1.219482),
            // withTooltip: latLng(47.41422, -1.250482),
            latlngs: [],
            currentZoom: 11.5,
            currentCenter: latLng(47.2243657, 38.9105216),
            showParagraph: true,
            mapOptions: {
                zoomSnap: 0.5,
                attributionControl: false,
            },
            showMap: true,
            staticAnchor: [16, 37],
            staticIconSize: [32, 37],
            errors: []
        };
    },
    created() {
        axios.get('api/v1/map/markers')
            .then(response => {
                console.log(response.data)
                for (var marker_info of response.data) {
                    var coords = marker_info.gps.split(',')
                    if (marker_info.marker_type === 0) {
                        this.latlngs.push(latLng(coords[0], coords[1], 1))
                    }
                }
                console.log(this.latlngs)
            })
            .catch(e => {
                this.errors.push(e)
                console.log(e)
            })
    },
    methods: {
        zoomUpdate(zoom) {
            this.currentZoom = zoom;
        },
        centerUpdate(center) {
            this.currentCenter = center;
        },
        showLongText() {
            this.showParagraph = !this.showParagraph;
        },
        innerClick() {
            alert("Click!")
        },
    },
    computed: {
        dynamicSize() {
            return [this.iconSize, this.iconSize]
        },
        dynamicAnchor() {
            return [this.iconSize / 2, this.iconSize]
        },
    }
}
</script>

<style scoped>

</style>