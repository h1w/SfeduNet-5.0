import Vue from 'vue'
import VueRouter from 'vue-router'
import MapView from '../views/MapView.vue'
import InstructionView from '../views/InstructionView.vue'
import VolunteeringView from '../views/VolunteeringView.vue'
import ContactsView from '../views/ContactsView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'map',
    component: MapView
  },
  {
    path: '/instruction/',
    name: 'instruction',
    component: InstructionView
  },
  {
    path: '/volunteering/',
    name: 'volunteering',
    component: VolunteeringView
  },
  {
    path: '/contacts/',
    name: 'contacts',
    component: ContactsView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
