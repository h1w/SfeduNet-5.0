<template>
    <div>  
        <l-map
        v-if="showMap"
        :zoom="zoom"
        :center="center"
        :options="mapOptions"
        @update:center="centerUpdate"
        @update:zoom="zoomUpdate"
        ref="mymap"
        >
            <l-tile-layer :url="url" :attribution="attribution" maxWidth="auto" />
            <l-marker v-for="(marker, index) in markers" :key="index" ref="myMarker" :lat-lng="marker.latLng">
                <l-icon
                :icon-size="staticIconSize"
                :icon-anchor="staticAnchor"
                :icon-url="markerIconSVG"
                >
                </l-icon>
                <l-popup>
                    <div>
                        <img id="marker-image" :src="marker.thumbnail" alt="..." />
                        <br>
                        <div class="container">
                            <div class="row">
                                <div class="col-md-12">
                                    <p class="text-center">{{ marker.street }}</p>
                                    <div class="d-flex justify-content-center">
                                        <br><br>
                                        <b-button class="delete-marker-button" variant="outline-danger" @click="deleteMarker(marker.id)">Удалить маркер</b-button>
                                        <!-- <b-button class="delete-marker-button" variant="outline-info" @click="testFunction()">test function</b-button> -->
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </l-popup>
            </l-marker>
            <l-control-zoom position="bottomright"  ></l-control-zoom>
        </l-map>
    </div>
</template>

<script>
import { latLng, icon } from 'leaflet'
import axios from 'axios'

export default {
    name: 'SimpleMap',
    data() {
        return {
            zoom: 12,
            center: latLng(47.2243657, 38.9105216),
            url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            attribution: '<a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            // withPopup: latLng(47.41322, -1.219482),
            // withTooltip: latLng(47.41422, -1.250482),
            markers: [],
            currentZoom: 11.5,
            currentCenter: latLng(47.2243657, 38.9105216),
            showParagraph: true,
            mapOptions: {
                zoomSnap: 0.5,
                attributionControl: false,
                zoomControl: false,
            },
            showMap: true,
            staticAnchor: [16, 37],
            staticIconSize: [26, 34],
            errors: [],
            markerIconSVG: require('@/assets/MarkerIcon2.svg'),
        };
    },
    created() {
        axios.get('api/v1/map/markers')
            .then(response => {
                console.log(response.data)
                for (var marker_info of response.data) {
                    var coords = marker_info.gps.split(',')
                    // var delete_link = "http://tagproject-api.sfedu.ru/api/v1/map/markers/delete/"+marker_info.id
                    this.markers.push(
                        {
                            'id': marker_info.id,
                            'street': marker_info.street,
                            'name': marker_info.name,
                            'description': marker_info.description,
                            'marker_type': marker_info.marker_type,
                            'latLng': latLng(coords[0], coords[1]),
                            'image': marker_info.get_image,
                            'thumbnail': marker_info.get_thumbnail,
                        }
                    )
                }
                console.log(this.markers)
            })
            .catch(e => {
                this.errors.push(e)
                console.log(e)
            })
        
        setTimeout(() => {
            this.$refs.mymap.mapObject.invalidateSize();
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
        deleteMarker(marker_id) {
            axios.delete(`https://tagproject-api.sfedu.ru/api/v1/map/markers/delete/${marker_id}`)
                .then(response => {
                    console.log(response);
                    this.$router.go()
                })
                .catch(function (error) {
                    console.log(error.response)
                })
        },
        // testFunction() {
        //     this.$router.go()
        // },
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