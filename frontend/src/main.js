import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'

import '@/assets/App.scss'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

import { Icon } from 'leaflet'
import { LMap, LTileLayer, LMarker, LPopup, LTooltip, LIcon, LControlZoom } from 'vue2-leaflet'

import "leaflet/dist/leaflet.css"

// import 'leaflet-fullscreen/dist/leaflet.fullscreen.css';
// import 'leaflet-fullscreen/dist/Leaflet.fullscreen';

Vue.component('l-map', LMap)
Vue.component('l-tile-layer', LTileLayer)
Vue.component('l-marker', LMarker)
Vue.component('l-popup', LPopup)
Vue.component('l-tooltip', LTooltip)
Vue.component('l-icon', LIcon)
Vue.component('l-control-zoom', LControlZoom)

delete Icon.Default.prototype._getIconUrl
Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
})

import axios from 'axios'

axios.defaults.baseURL = 'https://tagproject-api.sfedu.ru/'

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

import JsonCSV from 'vue-json-csv'

Vue.component('downloadCsv', JsonCSV)

import VueCookies from 'vue-cookies'

new Vue({
  axios,
  router,
  store,
  VueCookies,
  render: h => h(App)
}).$mount('#app')
