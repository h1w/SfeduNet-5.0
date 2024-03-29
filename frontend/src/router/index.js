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
import Cookies from 'js-cookie'

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
    path: '/login',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/myaccount',
    name: 'MyAccount',
    component: MyAccount,
    // meta: {
    //   requireLogin: true
    // }
  },
  {
    path: '/exportcsv',
    name: 'ExportCSV',
    component: ExportCSV,
    // meta: {
    //   requireLogin: true
    // }
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

// router.beforeEach(async (to, from, next) => {
//   // console.log(3333333)
//   // if (localStorage.getItem("isAuthenticated") === false) {
//   //   console.log(4444444444444)
//   //   store.refreshTokens()
//   // }
//   if (to.matched.some(record => record.meta.requireLogin)) {
//     if (!store.state.isAuthenticated) { // Если не авторизован
//       next({ name: 'LogIn', query: {to: to.path } });
//     }
//     else { // Если авторизован, нужно проверить валидность токенов и обновить access токен
//       var result = this.$store.commit("verifyToken", Cookies.get("refreshToken"))
//       if (result === true) { // Если refresh токен действителен, обновляем access токен
//         this.$store.commit("refreshAccessToken")
//       } else { // Если refresh токен не действителен, то удаляем все и просим пользователя пройти на страничку авторизации
//         Cookies.remove("accessToken")
//         Cookies.remove("refreshToken")

//         store.state.isAuthenticated = false;

//         next({ name: 'LogIn', query: {to: to.path } });
//       }
//     }
//   }
// })

router.beforeEach(async (to, from, next) => {
  if (store.state.isAuthenticated) {
    store.commit("verifyRefreshToken")
  }

  next()
})

// export const routeConfig = createRouter({
//   history: createWebHistory(),
//   routes: routes
// });

// router.beforeEach((to, from, next) => {
//   if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
//     next({ name: 'LogIn', query: { to: to.path } });
//   } else {
//     next()
//   }
// })

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
