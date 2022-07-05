import Vue from 'vue'
import VueRouter from 'vue-router'
import MapView from '../views/MapView.vue'
import InstructionView from '../views/InstructionView.vue'
import VolunteeringView from '../views/VolunteeringView.vue'
import AboutView from '../views/AboutView.vue'
import ContactsView from '../views/ContactsView.vue'
import LogIn from '../views/LogIn.vue'
import MyAccount from '../views/MyAccount.vue'
import ExportCSV from '../views/ExportCSV.vue'

import store from '@/store'

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
    path: '/about/',
    name: 'about',
    component: AboutView
  },
  {
    path: '/contacts/',
    name: 'contacts',
    component: ContactsView
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/export-csv',
    name: 'ExportCSV',
    component: ExportCSV,
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

// export const routeConfig = createRouter({
//   history: createWebHistory(),
//   routes: routes
// });

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})

// router.beforeEach(async (to, from, next) => {
//   let userProfile = store.getters["auth/getUserProfile"];
//   let isAuthenticated = localStorage.getItem("isAuthenticated");
//   if (userProfile.id === 0 && isAuthenticated) {
//     await store.dispatch("auth/userProfile");
//     userProfile = store.getters["auth/getUserProfile"];
//   }

//   if (to.meta.requireLogin) {
//     if (userProfile.id === 0) {
//       return next({ name: "LogIn" });
//     }
//   } else {
//     if (userProfile.id !== 0) {
//       return next({ name: "MyAccount" });
//     }
//   }
//   return next();
// });

export default router
