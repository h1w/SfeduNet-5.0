import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isAuthenticated: false,
    accessToken: null,
    refreshToken: null,
  },
  getters: {
  },
  mutations: {
    updateStorage(state, { access, refresh }) {
      state.accessToken = access
      state.refreshToken = refresh
    },
    async userLogin(state, usercredentials) {
      const formData = {
        username: usercredentials.username,
        password: usercredentials.password
      }
      await axios
        .post("/api/v1/auth/jwt/create/", formData)
        .then(response => {
          state.accessToken = response.data.access
          state.refreshToken = response.data.refresh
          state.isAuthenticated = true;
          console.log('status: authenticated')
        })
        .catch(err => {
          console.log(JSON.stringify(err))
        })
    },
    async refreshToken(state) {
      await axios
        .post("/api/v1/auth/jwt/refresh", formData)
        .then(response => {
          state.accessToken = response.data.access
          state.isAuthenticated = true;
        })
        .catch(err => {
          console.log(JSON.stringify(err))
        })
    },
    removeToken(state) {
      state.accessToken = null,
      state.refreshToken = null,
      state.isAuthenticated = null
      console.log('status: logout success')
    },
  },
  actions: {
  },
  modules: {
  }
})