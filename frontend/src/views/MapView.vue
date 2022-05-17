<template>
  <!-- <b-container> -->
    <div id="map-container">
      <SimpleMap />
    </div>
  <!-- </b-container> -->
</template>

<script>
import SimpleMap from '@/components/Map/SimpleMap.vue'

export default {
  name: 'MapView',
  data: function () {
    return {

    }
  },
  components: {
    SimpleMap,
  },
}
</script>

<style scoped>
#map-container {
  position: absolute;
  height: auto;
  width: 100%;
  top: 4.2em;
  bottom: 0;
  right: 0;
  left: 0;
}

#map-container > div {
  width: 100%;
  height: 100%;
}
</style>