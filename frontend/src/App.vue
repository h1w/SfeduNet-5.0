<template>
  <div id="app">
    <Navbar />
    <router-view/>
  </div>
</template>

<script>
import Navbar from '@/components/Navigation/Navbar.vue'

export default {
  name: 'app',
  components: {
    Navbar,
  },
}
</script>

<style lang="scss" scoped>
#app {
  font-family: 'Inter', sans-serif;
}
</style>